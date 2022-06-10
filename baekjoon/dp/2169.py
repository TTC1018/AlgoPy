in_range = lambda x, y: 0 <= x < N and 0 <= y < M


def dfs(x, y):
    if (x, y) == (0, 0):
        return graph[0][0]

    max_val = -101
    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if in_range(nx, ny):
            max_val = max(max_val, dfs(nx, ny))
    dp[x][y] += max_val
    return dp[x][y]


direc = [(0, -1), (0, 1), (-1, 0)]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[N - 1][M - 1] = graph[N - 1][M - 1]

visited = [[False] * M for _ in range(N)]
dfs(N - 1, M - 1)
print(dp[0][0])