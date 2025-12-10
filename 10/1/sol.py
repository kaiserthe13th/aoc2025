from itertools import combinations
import os
from typing import Self

class Circuit:
    expected: list[bool]
    buttons: list[list[int]]
    joltages: list[int]

    def __init__(self, expected: list[bool], buttons: list[list[int]], joltages: list[int]) -> None:
        self.expected = expected
        self.buttons = buttons
        self.joltages = joltages

    @classmethod
    def parse_str(cls, s: str) -> Self:
        parts = s.split(' ')
        expected = [i == '#' for i in parts[0][1:-1]]
        buttons = [[int(i) for i in part[1:-1].split(',')] for part in parts[1:-1]]
        joltages = [int(part) for part in parts[-1][1:-1].split(',')]
        return cls(expected, buttons, joltages)

    def fewest_presses_for_getting_expected(self) -> int:
        # from 0 to len(self.buttons), just try all combinations
        for press_count in range(len(self.buttons) + 1):
            for comb in combinations(self.buttons, press_count):
                state = [False] * len(self.expected)
                for c in comb:
                    for i in c:
                        state[i] = not state[i]
                if state == self.expected: # reached what we want
                    return press_count
        raise ValueError("unsolvable")

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = [Circuit.parse_str(line.strip()) for line in f.readlines() if line.strip()]

res = 0
for cir in inp:
    res += cir.fewest_presses_for_getting_expected()
print(res)
