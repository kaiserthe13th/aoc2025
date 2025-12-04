import os

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip() for line in f.readlines()]

res = 0

for i, line in enumerate(inp):
    for j, ch in enumerate(line):
        # if not a paper roll, no need to care
        if ch != '@':
            continue
        free_spot_count = 0

        for dy in range(-1, 2): # The positional change in dy
            for dx in range(-1, 2): # The positional change in dx
                if not (dx or dy): # Skip (0, 0)
                    continue
                y = i + dy
                x = j + dx
                # if the spot is not mapped, that means it's free
                if y < 0 or y >= len(inp) or x < 0 or x >= len(inp[y]):
                    free_spot_count += 1
                    continue
                # if the spot is free, that means it's free
                if inp[y][x] != '@':
                    free_spot_count += 1
        if free_spot_count > 4: # roll count is great enough
            res += 1

print(res)
