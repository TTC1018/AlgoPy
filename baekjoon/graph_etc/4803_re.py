import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def find_parent(node):
    if parent[node] == node:
        return node

    parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


case = 1
while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    parent = [i for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(a) == find_parent(b): # 사이클 생기는 경우
            union_parent(a, 0) # 0에 union 시키기 (트리 불가처리)
        else:
            union_parent(a, b)

    tree = 0
    checked = [False] * (n + 1)
    for i in range(1, n + 1):
        p = find_parent(i)
        if p != 0 and not checked[p]: # 부모가 0이 아니면 트리
            tree += 1
            checked[p] = True # 부모 중복체크 방지

    print('Case {}:'.format(case), end=' ')
    if tree > 1:
        print('A forest of {} trees.'.format(tree))
    elif tree == 1:
        print('There is one tree.')
    else:
        print('No trees.')
    case += 1