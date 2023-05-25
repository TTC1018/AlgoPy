import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
LOG = 21


def set_dist(now, depth):
    visited[now] = True
    dist_from_root[now] = depth

    for child in graph[now]:
        if not visited[child]:
            parent[child][0] = now
            set_dist(child, depth + 1)


def set_parent():
    set_dist(1, 0)
    for depth in range(1, LOG):
        for i in range(1, n + 1):
            parent[i][depth] = parent[parent[i][depth - 1]][depth - 1]



def lca(a, b):
    if dist_from_root[a] > dist_from_root[b]:
        a, b = b, a

    for depth in range(LOG - 1, -1, -1):
        if dist_from_root[b] - dist_from_root[a] >= (1 << depth):
            b = parent[b][depth]

    if a == b:
        return a

    for depth in range(LOG - 1, -1, -1):
        if parent[a][depth] != parent[b][depth]:
            a, b = parent[a][depth], parent[b][depth]

    return parent[a][0]


n = int(input())
parent = [[0] * LOG for _ in range(n + 1)]
dist_from_root = [0] * (n + 1)
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
