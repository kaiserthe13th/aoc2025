import os

def make_range(i):
    [start, stop] = i.split('-')
    return range(int(start), int(stop) + 1)

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    [ranges, availables] = f.read().split('\n\n')
    ranges = [make_range(i.strip()) for i in ranges.split('\n')]
    availables = [int(i.strip()) for i in availables.split('\n') if i.strip()]

def in_ranges(x: int, ranges: list[range]) -> bool:
    # iterate over ranges and check if x in r
    for r in ranges:
        if x in r:
            return True
    return False

res = 0
# brute force, idk or care if there is any better way this is more than fast enough for the input size
for avail in availables:
    if in_ranges(avail, ranges):
        res += 1

print(res)
