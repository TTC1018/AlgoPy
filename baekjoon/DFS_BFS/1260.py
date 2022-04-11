from copy import deepcopy
from collections import deque

def dfs(graph, start):
    for next in graph[start]:
        if not visited[next]:
            print(next + 1, end=' ')
            visited[next] = True
            dfs(graph, next)
        



N, M, V = map(int, input().split())
V -= 1

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
for i in range(N):
    graph[i].sort()

visited = [False] * N
visited[V] = True
print(V + 1, end=' ')
dfs(deepcopy(graph), V)

print()
#BFS
visited = [False] * N
visited[V] = True
print(V + 1, end=' ')

q = deque()
q.append(V)
while q:
    now = q.popleft()
    for next in graph[now]:
        if not visited[next]:
            print(next + 1, end=' ')
            visited[next] = True
            q.append(next)