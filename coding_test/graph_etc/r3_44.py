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

points[0].sort(), points[1].sort(), points[2].sort() # X, Y, Z 축 좌표 각각 정렬
edges = []
for i in range(N - 1):
    edges.append((points[0][i + 1][0] - points[0][i][0], points[0][i][1], points[0][i + 1][1])) # 정렬된 좌표간의 거리 = X축만 고려했을 때 최솟값을 가지는 간선들
    edges.append((points[1][i + 1][0] - points[1][i][0], points[1][i][1], points[1][i + 1][1]))
    edges.append((points[2][i + 1][0] - points[2][i][0], points[2][i][1], points[2][i + 1][1]))
edges.sort() # X/Y/Z 각각의 축만 고려한 간선값 후보라 중복되는 간선이 있을 수도 있음, 그러나 간선 값 기준으로 정렬 후에 크루스칼 알고리즘으로 사용하면 중복 선택이 예방됨

answer = 0
for e in edges:
    dist, A, B = e
    if find_parent(A) != find_parent(B):
        union_parent(A, B)
        answer += dist
print(answer)

