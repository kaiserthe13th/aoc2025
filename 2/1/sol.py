import os

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip().split('-') for line in f.read().split(',')]

res = 0
used = set() # to prevent reuse
for [a, b] in inp:
    start = int(a)
    stop = int(b)
    r = range(start, stop + 1)
    exp = 10 ** (len(a) // 2) # find the increment amount
    for i in range(start, stop + exp, exp): # iterate over the numbers that we can test candidates in
        s = str(i)
        ldiv, lmod = divmod(len(s), 2)
        if lmod == 1:
            # if it ain't zero, that means there is no way to split the number into
            # fixed-size non-overlapping chunks
            continue
        ck = int(s[:ldiv] * 2) # find what we get if we repeated the initials
        if ck in r and ck not in used: # if in range and not used already
            used.add(ck)
            res += ck

print(res)
