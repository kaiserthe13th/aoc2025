import os

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip() for line in f.readlines()]

res = 0

rot = 50 # starting rotation
for line in inp:
    # get value
    val = int(line[1:])
    if line.startswith('L'):
        # make positive
        val = 100 - val
    # apply mod rotation to get it to wrap-around
    rot = (rot + val) % 100
    if not rot:
        res += 1

print(res)
