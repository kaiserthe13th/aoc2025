import os

with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip() for line in f.readlines()]

res = 0

for line in inp:
    max_idx = 0
    for i, ch in enumerate(line[:-1]):
        if line[max_idx] < ch:
            max_idx = i
    xmax_idx_after = max_idx + 1
    for i, ch in enumerate(line[max_idx + 1:]):
        if line[xmax_idx_after] < ch:
            xmax_idx_after = max_idx + 1 + i
    t = int(line[max_idx]) * 10 + int(line[xmax_idx_after])
    print(t)
    res += t

print(f"Result: {res}")
