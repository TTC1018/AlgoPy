import sys
input = sys.stdin.readline


in_range = lambda x, y: 0 <= x < N and 0 <= y < N
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(2, N):
    if not graph[0][i]:
        dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, N):
    for j in range(2, N):
        if not graph[i][j]:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
            if not graph[i - 1][j] and not graph[i][j - 1]:
                dp[2][i][j] = dp[0][i - 1][j - 1] + dp[2][i - 1][j - 1] + dp[1][i - 1][j - 1]
print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])