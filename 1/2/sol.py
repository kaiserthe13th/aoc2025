import os

with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip() for line in f.readlines()]

res = 0
rot = 50
size = 100
for line in inp:
    dir = line[0]
    val = int(line[1:])
    res += val // size
    val %= size
    
    if dir == 'L':
        val *= -1
    
    if rot + val >= size or (rot > 0 and rot + val <= 0):
        res += 1

    rot = (rot + val) % size

print(res)
