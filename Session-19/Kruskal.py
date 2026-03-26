class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])  # path compression
        return self.parent[node]

    def unionByRank(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1


def spanningTree(V, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    ds = DSU(V)
    minCost = 0

    for edge in edges:
        u, v, w = edge

        if ds.findParent(u) != ds.findParent(v):
            minCost += w
            ds.unionByRank(u, v)

    return minCost


# Main
if __name__ == "__main__":
    V = 5

    edges = [
        [0, 1, 2],
        [0, 3, 6],
        [1, 2, 3],
        [1, 3, 8],
        [1, 4, 5],
        [2, 4, 7],
        [3, 4, 9]
    ]

    result = spanningTree(V, edges)

    print("Minimum Cost of MST:", result)
