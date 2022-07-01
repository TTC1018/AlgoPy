from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
S, E = map(int, input().split())

INF = int(1e9)
dist = [INF] * (n + 1)
dist[S] = 0

prev_node = [-1] * (n + 1)
q = [(0, S)]
while q:
    cost, now = heappop(q)
    if dist[now] < cost:
        continue

    for nxt, nxt_c in graph[now]:
        n_cost = cost + nxt_c
        if n_cost < dist[nxt]:
            prev_node[nxt] = now
            dist[nxt] = n_cost
            heappush(q, (n_cost, nxt))


print(dist[E])
answer = []
prev = E
while prev != S:
    answer.append(prev)
    prev = prev_node[prev]
answer.append(S)
print(len(answer))
print(*reversed(answer))