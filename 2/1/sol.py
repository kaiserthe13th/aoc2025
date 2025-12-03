import os

with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip().split('-') for line in f.read().split(',')]

res = 0
used = set()
for [a, b] in inp:
    start = int(a)
    stop = int(b)
    r = range(start, stop + 1)
    exp = 10 ** (len(a) // 2)
    for i in range(start, stop + exp, exp):
        s = str(i)
        ldiv, lmod = divmod(len(s), 2)
        if lmod == 1:
            continue
        ck = int(s[:ldiv] * 2)
        if ck in r and ck not in used:
            used.add(ck)
            res += ck

print(res)
