import os

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip() for line in f.readlines()]

res = 0
rot = 50 # starting rotation
size = 100 # it was getting out of hand, so made it a variable
for line in inp:
    dir = line[0] # separate direction
    val = int(line[1:])
    res += val // size
    val %= size
    
    if dir == 'L':
        val *= -1
    
    # this actually took a while to come up
    # if we passed the dial (+), or we had positive rotation and we passed the dial in reverse
    if rot + val >= size or (rot > 0 and rot + val <= 0):
        res += 1

    # apply mod rotation to get it to wrap-around
    rot = (rot + val) % size

print(res)
