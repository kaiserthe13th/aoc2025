import os


def parse_input(data: str) -> tuple[dict[int, list[tuple[int, int]]], list[tuple[tuple[int, int], list[int]]]]:
    sections = data.strip().split("\n\n")
    shapes = {}
    queries = []

    for section in sections:
        lines = section.split("\n")
        header = lines[0].strip()

        if header.endswith(":"): # is shape
            shape_idx = int(header[:-1])
            grid = []
            for r, line in enumerate(lines[1:]):
                for c, char in enumerate(line):
                    if char == "#":
                        grid.append((r, c))
            shapes[shape_idx] = grid
        elif "x" in header and ":" in header: # is fitting descriptor
            for line in lines:
                if not line.strip():
                    continue
                [dims, counts] = line.split(":")
                w, h = map(int, dims.split("x"))
                piece_counts = [int(i) for i in counts.strip().split()]
                queries.append(((w, h), piece_counts))

    return shapes, queries

# load input file
with open(os.path.join(__file__, "../input")) as f:
    inp = parse_input(f.read())

def normalize_coords(coords: list[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    # make coords so that the top left coord is at (0,0) and sort them
    if not coords:
        return tuple()
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    normalized = [(r - min_r, c - min_c) for r, c in coords]
    normalized.sort()
    return tuple(normalized)

def shape_variations_by_flip_and_rot(base_shape: list[tuple[int, int]]) -> list[tuple[tuple[int, int], ...]]:
    # flipped: F, rotated by <nn> degrees clockwise: <nn>deg
    # generates: 0deg, 90deg, F180deg, F270deg, F0deg, F90deg, F180deg, F270deg.
    variations = set()
    current = base_shape
    # try 4 rotations
    for _ in range(4):
        # rotate 90 degrees clockwise: (r, c): (c, -r)
        current = [(c, -r) for r, c in current]
        variations.add(normalize_coords(current))
        # flip horizontally: (r, c): (r, -c)
        flipped = [(r, -c) for r, c in current]
        variations.add(normalize_coords(flipped))
    return list(variations)

def fit_shapes_in_region(w: int, h: int, pieces_to_fit: list[int], occupied: set[tuple[int, int]], shape_variations: dict[int, list[tuple[tuple[int, int], ...]]]):
    if not pieces_to_fit:
        return True
    current = pieces_to_fit[0]
    remaining = pieces_to_fit[1:]
    variations = shape_variations[current] # get all shape variations for the shape

    # try every position
    for row in range(h):
        for col in range(w):
            if (row, col) in occupied:
                continue
            for var in variations:
                # check if this variation fits at anchor (r, c)
                fits = True
                new_taken = []
                for dr, dc in var:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < h and 0 <= nc < w): # bounds check
                        fits = False
                        break
                    if (nr, nc) in occupied: # no collisions
                        fits = False
                        break
                    new_taken.append((nr, nc))
                if fits:
                    for cell in new_taken: # place
                        occupied.add(cell)
                    if fit_shapes_in_region(w, h, remaining, occupied, shape_variations):
                        return True
                    for cell in new_taken: # backtrack if we can't fit
                        occupied.remove(cell)
    return False

def solve(inp: tuple[dict[int, list[tuple[int, int]]], list[tuple[tuple[int, int], list[int]]]]) -> int:
    shapes, queries = inp
    # precompute shape variations
    shape_variations: dict[int, list[tuple[tuple[int, int], ...]]] = {}
    for idx, grid in shapes.items():
        shape_variations[idx] = shape_variations_by_flip_and_rot(grid)
    res = 0
    for (w, h), counts in queries:
        pieces_list: list[int] = []
        total_area = 0
        for shape_id, count in enumerate(counts):
            for _ in range(count):
                pieces_list.append(shape_id)
                total_area += len(shapes[shape_id])
        # eliminate by area
        if total_area > w * h:
            continue
        pieces_list.sort(key=lambda sid: len(shapes[sid]), reverse=True)
        # try solution
        if fit_shapes_in_region(w, h, pieces_list, set(), shape_variations):
            res += 1
    return res

res = solve(inp)
print(res)
