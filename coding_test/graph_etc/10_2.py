def find_parent(node):
    if p_list[node] != node:
        return find_parent(p_list[node])
    return p_list[node]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        p_list[a] = b
    else:
        p_list[b] = a


N, M = map(int, input().split())
p_list = [i for i in range(N + 1)]


for _ in range(M):
    x, a, b = map(int, input().split())

    if x == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')