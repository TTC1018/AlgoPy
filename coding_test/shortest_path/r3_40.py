import heapq

INF = int(1e9)
N, M = map(int, input().split())
distance = [INF] * (N + 1)
distance[1] = 0

routes = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    routes[A].append(B)
    routes[B].append(A)

q = [(0, 1)]
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue
    for next in routes[now]:
        cost = dist + 1
        if cost < distance[next]:
            distance[next] = cost
            heapq.heappush(q, (cost, next))

min_dest, max_val, count = N, 0, 0
for i in range(1, N + 1):
    if distance[i] != INF:
        max_val = max(max_val, distance[i])
for i in range(1, N + 1):
    if distance[i] == max_val:
        min_dest = min(min_dest, i)
        count += 1

print(min_dest, max_val, count)