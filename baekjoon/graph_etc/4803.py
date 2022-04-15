INF = int(1e9)

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

case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    parent = [i for i in range(n + 1)]
    tree = dict()
    for i in range(1, n + 1):
        tree[i] = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        pa, pb = find_parent(a), find_parent(b)
        if pa != pb:
            if tree[pa] == -INF or tree[pb] == -INF:
                tree[pa] = tree[pb] = -INF
            union_parent(a, b)
        else:
            tree[pa] = -INF
            
    tree_sum = 0
    for i in range(1, n + 1):
        tree[find_parent(i)] += 1
    for i in range(1, n + 1):
        if tree[i] > 0:
            tree_sum += 1
        
    print("Case {}:".format(case), end=' ')
    if tree_sum == 0:
        print('No trees.')
    elif tree_sum == 1:
        print('There is one tree.')
    else:
        print('A forest of {} trees.'.format(tree_sum))
    
    case += 1