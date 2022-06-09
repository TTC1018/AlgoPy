from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


N = int(input())
T, M = map(int, input().split())
L = int(input())

INF = int(1e9)
graph = [[] for _ in range(N + 1)]

for _ in range(L):
    a, b, time, cost = map(int, input().split())
    graph[a].append((b, time, cost))
    graph[b].append((a, time, cost))

distcost = [[INF for _ in range(10000 + 1)] for _ in range(N + 1)]
distcost[1][0] = 0

q = [(0, 0, 1)]
while q:
    time, cost, now = heappop(q)
    if distcost[now][cost] < time:
        continue
    for nxt, n_t, n_c in graph[now]:
        tt, tc = time + n_t, cost + n_c
        if tt <= T and tc <= M:
            if tt < distcost[nxt][tc]:
                distcost[nxt][tc] = tt
                heappush(q, (tt, tc, nxt))

for i in range(M + 1):
    if distcost[N][i] <= T:
        print(i)
        sys.exit()
print(-1)