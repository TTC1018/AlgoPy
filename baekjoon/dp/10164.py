import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0)]
N, M, K = map(int, input().split())
KN, KM = divmod(K - 1, M)

dp = [[0] * M for _ in range(N)]
if K != 0:
    for i in range(KN + 1):
        dp[i][0] = 1
    for j in range(KM + 1):
        dp[0][j] = 1
    for i in range(1, KN + 1):
        for j in range(1, KM + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    for i in range(KN, N):
        dp[i][KM] = dp[KN][KM]
    for j in range(KM, M):
        dp[KN][j] = dp[KN][KM]
    for i in range(KN + 1, N):
        for j in range(KM + 1, M):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
else:
    dp = [[1] * M for _ in range(N)]
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[N - 1][M - 1])