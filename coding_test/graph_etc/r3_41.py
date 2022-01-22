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
parent = [n for n in range(N + 1)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            union_parent(i + 1, j + 1)


order = list(map(int, input().split()))

flag = True
for i in range(M - 1): # 모든 노드가 같은 부모를 가진다 = 같은 집합이다 = 싸이클
    if find_parent(order[i]) != find_parent(order[i + 1]):
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
