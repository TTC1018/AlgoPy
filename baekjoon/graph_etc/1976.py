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

N, M = int(input()), int(input())
parent = [i for i in range(N + 1)]
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 1:
            union_parent(i + 1, j + 1)

routes = list(map(int, input().split()))

flag = True
for i in range(1, len(routes)):
    if find_parent(routes[i]) != find_parent(routes[i - 1]):
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')