INF = int(1e9)
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def dfs(start, count):
    global answer

    x, y = start
    if count >= answer[x][y]:
        return

    for d in direction:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    answer[nx][ny] = min(answer[nx][ny], count + 1)
                    dfs((nx, ny), count + 1)
                    visited[nx][ny] = False


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

answer = [[INF] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            dfs((i, j), 0)

result = 0
for i in range(N):
    for j in range(M):
        if answer[i][j] != INF:
            result = max(result, answer[i][j])
print(result)