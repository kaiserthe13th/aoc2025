import os
import numpy as np

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = [line.split() for line in f.readlines() if line.strip()]

arr = np.array(inp)
tarr = arr.transpose()

res = 0
# because we transposed, we can just go line by line
for row in tarr:
    ls = []
    for n in row:
        # if we have an operator, do it, otherwise keep adding to the list
        if n == '*':
            res += np.array(ls).prod()
        elif n == '+':
            res += np.array(ls).sum()
        else:
            ls.append(int(n))
print(res)
