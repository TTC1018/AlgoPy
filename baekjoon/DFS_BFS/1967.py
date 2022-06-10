import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(now):
    global dist, endpoint

    if dist < visited[now]:
        dist = visited[now]
        endpoint = now

    for nxt, cost in graph[now]:
        if visited[nxt] == -1:
            visited[nxt] = visited[now] + cost
            dfs(nxt)


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    P, C, E = map(int, input().split())
    P -= 1
    C -= 1
    graph[P].append((C, E))
    graph[C].append((P, E))


visited = [-1] * n
visited[0] = 0
dist, endpoint = 0, 0
dfs(0)

visited = [-1] * n
visited[endpoint] = 0
dist = 0
dfs(endpoint)

print(dist)