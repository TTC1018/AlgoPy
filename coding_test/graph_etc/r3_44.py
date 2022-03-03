def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa


N = int(input())
parent = [i for i in range(N)]

points = [[], [], []]
for i in range(N):
    X, Y, Z = map(int, input().split())
    points[0].append((X, i))
    points[1].append((Y, i))
    points[2].append((Z, i))

points[0].sort(), points[1].sort(), points[2].sort()
edges = []
for i in range(N - 1):
    edges.append((points[0][i + 1][0] - points[0][i][0], points[0][i][1], points[0][i + 1][1]))
    edges.append((points[1][i + 1][0] - points[1][i][0], points[1][i][1], points[1][i + 1][1]))
    edges.append((points[2][i + 1][0] - points[2][i][0], points[2][i][1], points[2][i + 1][1]))
edges.sort()

answer = 0
for e in edges:
    dist, A, B = e
    if find_parent(A) != find_parent(B):
        union_parent(A, B)
        answer += dist
print(answer)

