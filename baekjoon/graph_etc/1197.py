import sys
from heapq import heappush, heappop
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


V, E = map(int, input().split())
parent = [i for i in range(V + 1)]

edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    heappush(edges, (C, A, B))

answer = 0
while edges:
    cost, A, B = heappop(edges)
    if find_parent(A) != find_parent(B):
        union_parent(A, B)
        answer += cost
print(answer)