import os

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp = {label: outputs.split(' ') for [label, outputs] in (line.strip().split(':') for line in f.readlines())}

def count_paths(graph: dict[str, list[str]], start: str, end: str):
    # stores: current_node: count
    memo: dict[str, int] = {}
    def dfs(current_node):
        # is it memoized
        if current_node in memo:
            return memo[current_node]
        # is it the end
        if current_node == end:
            return 1
        # subpaths
        total_paths = 0
        for neighbor in graph.get(current_node, []):
            total_paths += dfs(neighbor)
        # memoize
        memo[current_node] = total_paths
        return total_paths
    return dfs(start)

res = count_paths(inp, 'you', 'out')
print(res)
