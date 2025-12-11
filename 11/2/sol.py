import os

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = {label: outputs.split(' ') for [label, outputs] in (line.strip().split(':') for line in f.readlines())}

def count_paths(graph: dict[str, list[str]], start: str, end: str, passing_through: list[str]):
    # stores: (current_node, frozenset(nodes_left_to_visit)): count
    memo: dict[tuple[str, frozenset[str]], int] = {}
    required = frozenset(passing_through) # convert for immutability and hashing
    def dfs(current_node: str, remaining: frozenset):
        # if current node is needed, remove it, we found it now
        if current_node in remaining:
            remaining = remaining - {current_node}
        # is it memoized
        state = (current_node, remaining)
        if state in memo:
            return memo[state]
        # is it the end
        if current_node == end:
            # only if 'remaining' is empty does it mean we have a valid path
            return 1 if not remaining else 0
        # subpaths
        total_paths = 0
        for neighbor in graph.get(current_node, []):
            total_paths += dfs(neighbor, remaining)
        # memoize
        memo[state] = total_paths
        return total_paths
    return dfs(start, required)

res = count_paths(inp, 'svr', 'out', passing_through=['fft', 'dac'])
print(res)
