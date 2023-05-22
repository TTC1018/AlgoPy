import sys
input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
C = list(map(int, input().split()))
dp = [[INF] * (K + 1) for _ in range(N)]
for i in range(N):
    dp[i][0] = 0

if C[0] <= K:
    dp[0][C[0]] = 1

for i in range(1, N):
    for cafeine in range(1, K + 1):
        dp[i][cafeine] = min(dp[i][cafeine], dp[i - 1][cafeine])

        if C[i] <= cafeine:
            dp[i][cafeine] = min(dp[i][cafeine], dp[i - 1][cafeine - C[i]] + 1)

print(dp[N - 1][K] if dp[N - 1][K] != INF else -1)