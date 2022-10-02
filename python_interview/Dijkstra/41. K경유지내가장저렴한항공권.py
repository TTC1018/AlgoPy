from heapq import heappush, heappop
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for f, t, p in flights:
            graph[f].append((t, p))

        q = [(0, 0, src)]
        dist = [int(1e9)] * n
        dist[src] = 0

        while q:
            cost, passed, now = heappop(q)

            for nxt, weight in graph[now]:
                n_dist = cost + weight
                if passed <= k and dist[nxt] >= n_dist:
                    dist[nxt] = n_dist
                    heappush(q, (n_dist, passed + 1, nxt))

        if dist[dst] != int(1e9):
            return dist[dst]
        return -1

print(Solution().findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2))