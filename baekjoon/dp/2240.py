import sys
input = sys.stdin.readline

T, W = map(int, input().split())
dp = [[[0] * (W + 1) for _ in range(2)] for _ in range(T)]

first_p = int(input()) - 1
if first_p == 0:
    dp[0][0][0] = 1
elif first_p == 1:
    dp[0][1][1] = 1

for i in range(1, T):
    p = int(input()) - 1
    if p == 0:
        dp[i][0][0] = dp[i - 1][0][0] + 1
        for j in range(1, W + 1):
            dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j - 1]) + 1
            dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j - 1])
    elif p == 1:
        dp[i][1][0] = dp[i - 1][1][0] + 1
        for j in range(1, W + 1):
            dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j - 1]) + 1
            dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j - 1])

print(max(max(dp[T-1][0]), max(dp[T-1][1])))