import os

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp: list[tuple[int, int]] = [tuple(int(i) for i in line.strip().split(',')) for line in f.readlines()] # type: ignore

max_start, max_end = 0, 0 
max_area = -1

def area(start: tuple[int, int], end: tuple[int, int]) -> int:
    # + 1 added because the points are inclusive
    return (abs(start[0] - end[0]) + 1) * (abs(start[1] - end[1]) + 1)

for i, start in enumerate(inp):
    for j, end in enumerate(inp[i + 1:]):
        cur_area = area(start, end)
        if max_area < cur_area:
            max_area = cur_area
            max_start = i
            max_end = i + 1 + j

print(inp[max_start])
print(inp[max_end])
print(max_area)
