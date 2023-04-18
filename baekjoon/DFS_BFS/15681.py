import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(now):
    if len(graph[now]) == 1 and visited[graph[now][0]]:
        tree[now] = 1
        return 1

    sum_val = 0
    for child in graph[now]:
        if not visited[child]:
            visited[child] = True
            sum_val += dfs(child)
            visited[child] = False
    tree[now] = sum_val + 1
    return tree[now]


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N)]
tree = [0] * N
visited = [False] * N
for _ in range(N - 1):
    U, V = map(lambda x: int(x) - 1, input().split())
    graph[U].append(V)
    graph[V].append(U)

visited[R - 1] = True
dfs(R - 1)
for _ in range(Q):
    print(tree[int(input()) - 1])
