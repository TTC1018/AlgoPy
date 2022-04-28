from heapq import heappush, heappop
import sys
input = sys.stdin.readline


INF = int(1e9)
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
distance[X] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    

q = [(X, 0)]
while q:
    now, dist = heappop(q)
    if distance[now] < dist:
        continue
    for nxt in graph[now]:
        n_dist = dist + 1
        if n_dist < distance[nxt]:
            distance[nxt] = n_dist
            heappush(q, (nxt, n_dist))

answer = [i for i, n in enumerate(distance) if n == K]
if len(answer) > 0:
    for a in answer:
        print(a)
else:
    print(-1)