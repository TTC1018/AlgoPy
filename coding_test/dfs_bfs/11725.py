import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(node):
    for nxt in edges[node]:
        if parent[nxt] == -1:
            edges[nxt].remove(node)
            parent[nxt] = node
            dfs(nxt)


N = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    C, P = map(int, input().split())
    edges[C].append(P)
    edges[P].append(C)
parent = [-1] * (N + 1)
parent[1] = 1

dfs(1)
for i in range(2, N + 1):
    print(parent[i])