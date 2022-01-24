def find_parent(node):
    if parent[node] != node:
        return find_parent(parent[node])
    return parent[node]


def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)

    if px > py:
        parent[px] = py
    else:
        parent[py] = px


N = int(input())
M = int(input())

parent = [n for n in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    union_parent(a, b)

count = 0
for i in range(2, N + 1):
    if find_parent(i) == 1:
        count += 1
print(count)