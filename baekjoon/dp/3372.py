import sys
input = sys.stdin.readline
d = [(1, 0), (0, 1)]

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    if i + B[0][i] < N:
        dp[0][i + B[0][i]] += dp[0][i]
    if B[0][i] < N:
        dp[B[0][i]][i] += dp[0][i]

for i in range(1, N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break

        if i + B[i][j] < N:
            dp[i + B[i][j]][j] += dp[i][j]
        if j + B[i][j] < N:
            dp[i][j + B[i][j]] += dp[i][j]
print(dp[N - 1][N - 1])