import sys
input = sys.stdin.readline


def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

c_flag = False
for i in range(m):
    a, b = map(int, input().split())
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
    else:
        print(i + 1)
        c_flag = True
        break

if not c_flag:
    print(0)