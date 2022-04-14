import sys
input = sys.stdin.readline
def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa == pb:
        return
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
max_w = [0 for i in range(N + 1)]

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
start, end = map(int, input().split())

edges.sort(reverse=True) # 일반 크루스칼과 다르게 최댓값부터 탐색
for e in edges:
    C, A, B = e
    union_parent(A, B)
    if find_parent(start) == find_parent(end):
        print(C)
        break