from heapq import heappush, heappop
import sys
input = sys.stdin.readline


INF = int(1e9)
N, M, X = map(int, input().split())
distance = [INF] * (N + 1)
distance[X] = 0

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A].append((B, T))
    

q = [(0, X)]
while q:
    dist, now = heappop(q)
    
    if distance[now] < dist:
        continue
    for nxt, cost in graph[now]:
        n_dist = dist + cost
        if n_dist < distance[nxt]:
            distance[nxt] = n_dist
            heappush(q, (n_dist, nxt))


dist_to_X = [INF] * (N + 1)
dist_to_X[X] = 0
for i in [n for n in range(1, N + 1) if n != X]:
    q = [(0, i)]
    distance_tmp = [INF] * (N + 1)
    distance_tmp[i] = 0
    while q:
        dist, now = heappop(q)
        if now == X:
            dist_to_X[i] = dist
            break
        if distance_tmp[now] < dist:
            continue
        for nxt, cost in graph[now]:
            n_dist = dist + cost
            if distance_tmp[nxt] > n_dist:
                distance_tmp[nxt] = n_dist
                heappush(q, (n_dist, nxt))

answer = [distance[i] + dist_to_X[i] for i in range(1, N + 1)]
print(max(answer))