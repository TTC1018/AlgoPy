def dfs(x, y):
    if not (0 <= x < N and 0 <= y < M):
        return False
    if g[x][y] == 0 and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


N, M = map(int, input().split())
g = []
for i in range(N):
    g.append(list(map(int, input())))
visited = [[0] * M for i in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            answer += 1
print(answer)