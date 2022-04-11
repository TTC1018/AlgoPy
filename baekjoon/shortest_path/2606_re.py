# 다익스트라 풀이법
from heapq import heappush, heappop

INF = int(1e9)
N, M = int(input()), int(input())

graph = [[] for _ in range(N)]
distance = [INF] * N
distance[0] = 0
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = [(0, 0)]
while q:
    now, cost = heappop(q)
    if distance[now] < cost:
        continue
    for next, dist in graph[now]:
        n_dist = cost + dist
        if n_dist < distance[next]:
            distance[next] = n_dist
            heappush(q, (next, n_dist))
print(N - distance.count(INF) - 1)