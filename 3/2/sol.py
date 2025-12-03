import os

with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.strip() for line in f.readlines()]

res = 0

def sol_line(line: str, dig_count: int, start: int, prefix: str):
    if dig_count <= 0:
        return int(prefix)
    nline = line[start:] if dig_count == 1 else line[start:-(dig_count - 1)]
    max_idx = 0
    for i, ch in enumerate(nline):
        if nline[max_idx] < ch:
            max_idx = i
    return sol_line(line, dig_count - 1, start = start + max_idx + 1, prefix = prefix + nline[max_idx])

for line in inp:
    t = sol_line(line, 12, 0, "")
    print(t)
    res += t

print(f"Result: {res}")
