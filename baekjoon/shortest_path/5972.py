from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
E = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    E[a].append((b, c))
    E[b].append((a, c))

D = [int(1e9)] * (N + 1)
D[1] = 0
q = [(0, 1)]
while q:
    dist, now = heappop(q)

    for nxt, cost in E[now]:
        new_cost = dist + cost
        if new_cost < D[nxt]:
            D[nxt] = new_cost
            heappush(q, (new_cost, nxt))

print(D[N])