import os
import numpy as np

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    # take the input with empty lines removed, and the ending '\n' also removed, and turn the string into an array
    inp = [[*i.removesuffix('\n')] for i in f.readlines() if i.strip()]
    # make a matrix of strand transpose
    inpm = np.array(inp, dtype=np.str_)
    tinpm = inpm.transpose()

print(tinpm)

res = 0
# store a list of history
prev_nums = [0]
prev_op = '+'
for line in tinpm:
    # get the current line
    ms = ''.join(line)
    n = ms[:-1] # this is the number
    nop = ms[-1] # the last char is the operator (if exists)
    if nop != ' ': # if we have an operator
        if prev_op == '+':
            res += sum(prev_nums)
        elif prev_op == '*':
            res += np.array(prev_nums).prod()
        prev_op = nop
        prev_nums = [int(n)]
        continue
    if n.strip(): # if the line is non-empty
        prev_nums.append(int(n)) # append to the list

# do the last one manually as it shouldn't be covered
if prev_op == '+':
    res += sum(prev_nums)
elif prev_op == '*':
    res += np.array(prev_nums).prod()

print(res)
