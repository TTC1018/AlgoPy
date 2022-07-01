from heapq import heappush, heappop
from collections import deque
import sys
input = sys.stdin.readline


def find_parent(node):
    if parent[node] == node:
        return node

    parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


N, M = map(int, input().split())
s, e = map(int, input().split())
parent = [i for i in range(N + 1)]
edges = []
for _ in range(M):
    h1, h2, k = map(int, input().split())
    heappush(edges, (-k, h1, h2))

# 최대 신장 트리로 연결
mst = [[] for _ in range(N + 1)]
cnt = 0
while edges and cnt < N - 1:
    cost, a, b = heappop(edges)
    if find_parent(a) != find_parent(b):
        cnt += 1
        union_parent(a, b)
        mst[a].append((b, -cost))
        mst[b].append((a, -cost))


q = deque()
q.append((s, int(1e9)))
visited = [False] * (N + 1)
visited[s] = True
answer = 0
while q:
    now, cost = q.popleft()
    if now == e:
        answer = max(answer, cost)
        continue

    for nxt, n_cost in mst[now]:
        if not visited[nxt] and n_cost >= answer:
            visited[nxt] = True
            q.append((nxt, min(cost, n_cost)))
print(answer)