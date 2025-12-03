import os

with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip().split('-') for line in f.read().split(',')]

res = 0
used = set()
for [a, b] in inp:
    start = int(a)
    stop = int(b)
    r = range(start, stop + 1)
    def try_split(split_count: int):
        global res
        exp = 10 ** (len(a) // split_count)
        for i in range(start, stop + exp, exp):
            s = str(i)
            ldiv, lmod = divmod(len(s), split_count)
            if lmod != 0:
                continue
            ck = int(s[:ldiv] * split_count)
            if ck in r and ck not in used:
                used.add(ck)
                res += ck
    for i in range(2, len(b) + 1):
        try_split(i)

print(res)
