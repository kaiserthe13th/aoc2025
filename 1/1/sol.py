import os

with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip() for line in f.readlines()]

res = 0

rot = 50
for line in inp:
    val = int(line[1:])
    if line.startswith('L'):
        val = 100 - val
    rot = (rot + val) % 100
    if not rot:
        res += 1

print(res)
