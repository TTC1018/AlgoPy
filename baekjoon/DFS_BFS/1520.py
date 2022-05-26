import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, y):
    global answer
    if x == M - 1 and y == N - 1:
        dp[x][y] = 1
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        if x > 0 and graph[x - 1][y] < graph[x][y]:
            dp[x][y] += dfs(x - 1, y)
        if x < M - 1 and graph[x + 1][y] < graph[x][y]:
            dp[x][y] += dfs(x + 1, y)
        if y > 0 and graph[x][y - 1] < graph[x][y]:
            dp[x][y] += dfs(x, y - 1)
        if y < N - 1 and graph[x][y + 1] < graph[x][y]:
            dp[x][y] += dfs(x, y + 1)
    return dp[x][y]


direc = [(-1, 0), (0, 1), (0, -1), (1, 0)]
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
answer = 0
dp = [[-1] * N for _ in range(M)]
dfs(0, 0)
print(dp[0][0])