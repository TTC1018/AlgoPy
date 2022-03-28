import heapq


def find_parent(node):
    if parent[node] != node:
        return find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa


N, M = map(int, input().split())
edges = []
total = 0
for _ in range(M):
    X, Y, Z = map(int, input().split())
    heapq.heappush(edges, (Z, X, Y))
    total += Z

parent = [i for i in range(N)]
answer, count = 0, 0
while count != N - 1:
    dist, X, Y = heapq.heappop(edges)
    if find_parent(X) != find_parent(Y): # 사이클 아니면
        count += 1
        answer += dist
        union_parent(X, Y)
print(total - answer)