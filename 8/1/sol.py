import math
import os

Vec3 = tuple[int, int, int]

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    inp: list[Vec3] = [tuple(int(i) for i in line.strip().split(",")) for line in f.readlines() if line.strip()] # type: ignore


class CircuitSet:
    def __init__(self, n):
        # parent[i] is the parent of i
        self.parent = list(range(n))
        # size[i] is the size of the set rooted at i
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # merge the smaller set into the larger one
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i

            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True  # union happened
        return False  # already in the same set

def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

def solve(coords: list[Vec3], num_connections=1000):
    coord_count = len(coords)
    if coord_count < 2:
        return 0 # not enough boxes for connections

    edges = [] # [(distance_squared, index1, index2)]

    # for all pairs (i, j) where i < j
    for i in range(coord_count):
        for j in range(i + 1, coord_count):
            d_sq = dist_sq(coords[i], coords[j])
            edges.append((d_sq, i, j))
    edges.sort()

    uf = CircuitSet(coord_count)

    for i in range(min(num_connections, len(edges))):
        _, u, v = edges[i]
        uf.union(u, v)

    # get the size of every circuit
    circuit_sizes = []
    # only consider the root nodes as they hold the size of the whole set
    for i in range(coord_count):
        if uf.parent[i] == i:
            circuit_sizes.append(uf.size[i])

    circuit_sizes.sort(reverse=True) # descending sort
    if len(circuit_sizes) >= 3:
        top_three = circuit_sizes[:3]
        return math.prod(top_three)
    elif len(circuit_sizes) > 0:
        return math.prod(circuit_sizes)
    else:
        return -1

res = solve(inp)
print(res)
