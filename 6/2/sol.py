import os
import numpy as np

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = [[*i.removesuffix('\n')] for i in f.readlines() if i.strip()]
    inpm = np.array(inp, dtype=np.str_)
    tinpm = inpm.transpose()

print(tinpm)

res = 0
prev_nums = [0]
prev_op = '+'
for line in tinpm:
    ms = ''.join(line)
    n = ms[:-1]
    nop = ms[-1]
    if nop != ' ':
        if prev_op == '+':
            res += sum(prev_nums)
        elif prev_op == '*':
            res += np.array(prev_nums).prod()
        prev_op = nop
        prev_nums = [int(n)]
        continue
    if n.strip():
        prev_nums.append(int(n))


if prev_op == '+':
    res += sum(prev_nums)
elif prev_op == '*':
    res += np.array(prev_nums).prod()

print(res)
