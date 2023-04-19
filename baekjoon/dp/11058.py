import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
if N <= 6:
    print(N)
else:
    for i in range(1, 6 + 1):
        dp[i] = i
    for i in range(7, N + 1):
        for j in range(3, i):
            dp[i] = max(dp[i], (j - 1) * dp[i - j])
    print(dp[N])