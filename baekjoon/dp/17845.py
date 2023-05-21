import sys
input = sys.stdin.readline


N, K = map(int, input().split())
L = [tuple(map(int, input().split())) for _ in range(K)]
dp = [[0] * (N + 1) for _ in range(K)]

if N >= L[0][1]:
    dp[0][L[0][1]] = L[0][0]

for i in range(1, K):
    for time in range(1, N + 1):
        dp[i][time] = max(dp[i][time], dp[i - 1][time])

        if L[i][1] <= time:
            dp[i][time] = max(dp[i][time], dp[i - 1][time - L[i][1]] + L[i][0])
print(max(dp[K - 1]))