import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


INF = int(1e9)
N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(C)
cityCount, distSum = 0, 0
for d in distance:
    if d != INF:
        cityCount += 1
        distSum = max(distSum, d)
print(cityCount - 1, distSum)