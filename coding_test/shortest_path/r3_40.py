import heapq

INF = int(1e9)
N, M = map(int, input().split())

routes = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    routes[A].append(B)
    routes[B].append(A)

distance = [INF] * (N + 1)
distance[1] = 0

q = []
for i in range(1, N + 1):
    if routes[1][i]:
        q.append((1, i))

while q:
    cost, now = heapq.heappop(q)

    if distance[now] < cost:
        continue
    for next in routes[now]:
        if cost < distance[next]:
            distance[next] = cost
            heapq.heappush(q, (cost + 1, next))

min_dest, max_val = N + 1, 0
for i in range(N + 1):
    if distance[i] != INF:
        max_val = max(max_val, distance[i])
        min_dest = min(min_dest, i)
print(min_dest, max_val, distance.count(max_val))