import sys
input = sys.stdin.readline


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * N for _ in range(M)]

answer = 0

for i in range(M):
    if graph[i][0] == 0:
        answer = 1
        dp[i][0] = 1
for i in range(N):
    if graph[0][i] == 0:
        answer = 1
        dp[0][i] = 1

for i in range(1, M):
    for j in range(1, N):
        if graph[i][j] == 0:
            dp[i][j] = max(dp[i][j], min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1)
        answer = max(answer, dp[i][j])

print(answer)