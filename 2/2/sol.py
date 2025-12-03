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
    def try_split(split_count: int):
        # so the logic here is the split_count is the following:
        # - we find an increment which is the step we use
        #   and it is selected to be whatever the following diagram:
        # 
        #   for example if we had '481293':
        #       with split_count = 2 => gives us 10 ** (6 - 6 // 2) = 10 ** 3 = 1000  as it splits it into '481' '293'
        #       with split_count = 3 => gives us 10 ** (6 - 6 // 3) = 10 ** 4 = 10000 as it splits it into '48' '12' '93'
        global res
        exp = 10 ** (len(a) - len(a) // split_count) # find the increment amount
        for i in range(start, stop + exp, exp): # iterate over the numbers that we can test candidates in
            s = str(i)
            ldiv, lmod = divmod(len(s), split_count)
            if lmod != 0:
                # if it ain't zero, that means there is no way to split the number into
                # fixed-size non-overlapping chunks
                continue
            ck = int(s[:ldiv] * split_count) # find what we get if we repeated the initials
            if ck in r and ck not in used: # if in range and not used already
                used.add(ck)
                res += ck
    for i in range(2, len(b) + 1): # try to split the number into 2, 3, 4, ..., up to and including len(b) parts and try
        try_split(i)

print(res)
