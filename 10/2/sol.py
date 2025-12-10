import os
from typing import Self
import z3

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

    def fewest_presses_for_getting_joltage(self) -> int:
        # this is an optimisation problem
        opt = z3.Optimize()

        # button_{i} is press the press count of the button
        press_counts = [z3.Int(f'button_{i}') for i in range(len(self.buttons))]

        # buttons can only be pressed 0 or more times
        for x in press_counts:
            opt.add(x >= 0)

        for i, joltage in enumerate(self.joltages): # press count sum is target joltage
            # Gather all button presses that contribute to this specific wire
            button_sum = 0
            for btn_idx, btn_targets in enumerate(self.buttons):
                if i in btn_targets:
                    # if button affects this joltage, add its variable to the sum
                    button_sum += press_counts[btn_idx]
            opt.add(button_sum == joltage) # total sum is target voltage

        # we now have a list of linear equations lists
        # which we must minimize the total of the press counts
        total_presses = z3.Sum(press_counts)
        opt.minimize(total_presses)

        result = opt.check() # find result
        if result == z3.sat:
            return opt.model().eval(total_presses).as_long() # return result as integer
        else:
            raise ValueError("unsolvable")

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = [Circuit.parse_str(line.strip()) for line in f.readlines() if line.strip()]

res = 0
for cir in inp:
    print(cir.joltages)
    res += cir.fewest_presses_for_getting_joltage()
print(res)
