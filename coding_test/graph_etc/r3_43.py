INF = int(1e9)


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

# 최소 신장 트리 = 크루스칼 알고리즘
N, M = map(int, input().split())
parent = [i for i in range(N)]

edges = []
total = 0
for _ in range(M):
    X, Y, Z = map(int, input().split())
    edges.append((Z, X, Y))
    total += Z

edges.sort()
answer = 0
for e in edges:
    cost, a, b = e
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost
print(total - answer) # 절약된 금액을 구하는 문제이므로 전체 금액 합 - 신장 트리 금액 합이 답임
