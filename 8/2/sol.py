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
        self.circ_count = n # circuit count

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
            self.circ_count -= 1
            return True # union happened
        return False # already in the same set

def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

def calculate_edges(coords: list[Vec3]) -> list[tuple[int, int, int]]:
    coord_count = len(coords)
    edges = [] # [(distance_squared, index1, index2)]

    # for all pairs (i, j) where i < j
    for i in range(coord_count):
        for j in range(i + 1, coord_count):
            d_sq = dist_sq(coords[i], coords[j])
            edges.append((d_sq, i, j))

    edges.sort()
    return edges

def solve(coords: list[Vec3]) -> int:
    coord_count = len(coords)
    if coord_count < 2:
        return 0 # not enough boxes for connections

    edges = calculate_edges(coords)
    uf = CircuitSet(coord_count)

    # until just one circuit remains
    last_edge_coords = None
    for _, u_idx, v_idx in edges:
        if uf.union(u_idx, v_idx): # if something was merged
            if uf.circ_count == 1:
                last_edge_coords = (coords[u_idx], coords[v_idx])
                break

    if last_edge_coords:
        # the last edge nodes' x coords
        x1 = last_edge_coords[0][0]
        x2 = last_edge_coords[1][0]
        return x1 * x2
    else:
        return 0

res = solve(inp)
print(res)
