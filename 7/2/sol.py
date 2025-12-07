import os

with open(os.path.join(__file__, "../../input")) as f:
    lines = f.read().splitlines()
    inp = [list(line.strip()) for line in lines if line.strip()]

spos = None
rows = len(inp)
cols = len(inp[0])

# find s
for i, s in enumerate(inp):
    if 'S' in s:
        spos = (i, s.index('S'))
        break

if spos is None:
    raise ValueError("S not found")

Position = tuple[int, int]

def descend(spos: Position, grid: list[list[str]], visited: dict[Position, int] | None = None):
    if visited is None:
        visited = {}

    # well, this is not bfs, that's awkward.
    y, x = spos
    if (y, x) in visited:
        return visited[(y, x)]

    paths = [(y + 1, x - 1), (y + 1, x + 1)] if grid[y][x] == '^' else [(y + 1, x)]

    res = 0
    has_child = False

    for ny, nx in paths:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]): # is within grid?
            has_child = True
            res += descend((ny, nx), grid, visited)

    if not has_child:
        res = 1

    visited[(y, x)] = res
    return res

res = descend((spos[0] + 1, spos[1]), inp)

print(res)
