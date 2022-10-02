from heapq import heappush, heappop
from typing import List


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def end_check():
            for d in dist:
                if d == int(1e9):
                    return False
            return True

        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]
        dist = [int(1e9)] * (n + 1)
        dist[0] = -1
        dist[k] = 0
        while q:
            cost, now = heappop(q)

            for nxt, weight in graph[now]:
                n_cost = cost + weight
                if n_cost < dist[nxt]:
                    dist[nxt] = n_cost
                    heappush(q, (n_cost, nxt))

        if end_check():
            return max(dist)
        else:
            return -1
