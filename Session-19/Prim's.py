import heapq

def spanningTree(V, edges):
    # Create adjacency list
    adj = [[] for _ in range(V)]

    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    visited = [False] * V
    pq = []

    # (weight, node)
    heapq.heappush(pq, (0, 0))

    minCost = 0

    while pq:
        wi, ui = heapq.heappop(pq)

        if visited[ui]:
            continue

        visited[ui] = True
        minCost += wi

        for currW, vi in adj[ui]:
            if not visited[vi]:
                heapq.heappush(pq, (currW, vi))

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
