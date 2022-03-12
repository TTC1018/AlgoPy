import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

#다익스트라
q = [(0, K)]
distance[K] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next, n_cost in graph[now]:
        n_dist = dist + n_cost
        if distance[next] > n_dist:
            distance[next] = n_dist
            heapq.heappush(q, (n_dist, next))

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])