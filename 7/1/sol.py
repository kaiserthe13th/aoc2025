import os
from collections import deque

with open(os.path.join(__file__, "../../input")) as f:
    lines = f.read().splitlines()

inp = [list(line.strip()) for line in lines if line.strip()]

spos = None

# find s
for i, s in enumerate(inp):
    if 'S' in s:
        spos = (i, s.index('S'))
        break

if spos is None:
    raise ValueError("S not found")

def descend(spos: tuple[int, int]):
    # wait, it's all bfs? always has been.
    y, x = spos
    if not (0 <= y < len(inp) and 0 <= x < len(inp[0])):
        return 0 # nowhere to descend

    visited = set()
    queue = deque([(y, x)])
    result = 0

    while queue:
        y, x = queue.popleft()
        if not (0 <= y < len(inp) and 0 <= x < len(inp[0])) or (y, x) in visited:
            continue
        
        # visit
        visited.add((y, x))
        current_char = inp[y][x]

        # decide next moves
        if current_char == '^': # split
            result += 1
            queue.append((y, x + 1))
            queue.append((y, x - 1))
        else:
            queue.append((y + 1, x)) # down
        
    return result

res = descend((spos[0] + 1, spos[1]))

print(res)
