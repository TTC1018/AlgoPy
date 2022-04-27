import sys
input = sys.stdin.readline


N = int(input())
dp = [[1] * 10 for _ in range(N + 1)]
dp[1][0] = 0
# 길이가 N이고, 마지막 숫자 L

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1]
    for j in range(1, 8 + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 10**9
    dp[i][9] = dp[i - 1][8]
print(sum(dp[N]) % 10**9)