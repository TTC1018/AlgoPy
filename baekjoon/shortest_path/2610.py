from collections import defaultdict

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

INF = int(1e9)
N, M = [int(input()) for _ in range(2)]
parent = [i for i in range(N + 1)]
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

# 거리 초기화 및 위원회 결성
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B], graph[B][A]  = 1, 1
    union_parent(A, B)
 

# 플루이드 워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 대표 선출
represent = defaultdict(list)
for i in range(1, N + 1):
    temp_dist = -1
    for j in range(1, N + 1):
        if graph[i][j] != INF:
            temp_dist = max(temp_dist, graph[i][j])
    if len(represent[find_parent(i)]) == 0:
        represent[find_parent(i)].extend([i, temp_dist])
    else:
        if temp_dist < represent[find_parent(i)][1]:
            represent[find_parent(i)] = [i, temp_dist]

represent = represent.values()
represent = list(map(lambda x:x[0], represent))
print(len(represent))
represent.sort()
for r in represent:
    print(r)