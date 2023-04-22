import sys
input = sys.stdin.readline
MOD = 1000000007

N, M = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    dp[i] += dp[i - 1]
    if i - M >= 0:
        dp[i] += dp[i - M]
    dp[i] %= MOD
print(dp[N])