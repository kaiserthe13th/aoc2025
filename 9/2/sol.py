import os

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp: list[tuple[int, int]] = [tuple(int(i) for i in line.strip().split(',')) for line in f.readlines()] # type: ignore

max_start, max_end = 0, 0 
max_area = -1

edges = []
for i, j in enumerate(inp):
    p1 = j
    p2 = inp[(i + 1) % len(inp)] # Wrap around to 0
    edges.append((p1, p2))

def area(start: tuple[int, int], end: tuple[int, int]) -> int:
    # + 1 added because the points are inclusive
    return (abs(start[0] - end[0]) + 1) * (abs(start[1] - end[1]) + 1)

def is_inside_polygon(start: tuple[int, int], end: tuple[int, int], edges: list[tuple[tuple[int, int], tuple[int, int]]]) -> bool:
    mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    intersection_count = 0
    # do horizontal rays and boundary checks
    for (x0, y0), (x1, y1) in edges:
        if x0 == x1: # if vertical edge
            # if within range and to the right of the midpoint
            if min(y0, y1) < mid[1] < max(y0, y1) and x1 > mid[0]:
                intersection_count += 1
    return bool(intersection_count % 2)

def edge_cut_through(start: tuple[int, int], end: tuple[int, int], edges: list[tuple[tuple[int, int], tuple[int, int]]]) -> bool:
    rxmin, rxmax = min(start[0], end[0]), max(start[0], end[0])
    rymin, rymax = min(start[1], end[1]), max(start[1], end[1])

    for (x0, y0), (x1, y1) in edges:
        if x0 == x1: # if vertical edge
            # rxmin < x0 < rxmax is quicker to check
            # which is why it is used as a heuristic to eliminate before actual check
            if rxmin < x0 < rxmax and max(min(y0, y1), rymin) < min(max(y0, y1), rymax): # strict check
                return True
        else: # if horizontal edge
            # same logic as above, just axisses flipped
            if rymin < y0 < rymax and max(min(x0, x1), rxmin) < min(max(x0, x1), rxmax):
                return True

    return False

for i, start in enumerate(inp):
    for j, end in enumerate(inp[i + 1:]):
        cur_area = area(start, end)
        if max_area < cur_area and is_inside_polygon(start, end, edges) and not edge_cut_through(start, end, edges):
            max_area = cur_area
            max_start = i
            max_end = i + 1 + j

print(inp[max_start])
print(inp[max_end])
print(max_area)
