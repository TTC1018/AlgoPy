X = int(input())

dp = [0] * (X + 1)
dp[1], dp[2], dp[3], dp[4], dp[5] = 0, 1, 1, 2, 1

for i in range(6, X + 1):

    if i % 5 == 0:
        dp[i] = dp[i // 5] + 1

    if i % 3 == 0:
        dp[i] = dp[i // 3] + 1 if dp[i] == 0 else min(dp[i], dp[i // 3] + 1)

    if i % 2 == 0:
        dp[i] = dp[i // 2] + 1 if dp[i] == 0 else min(dp[i], dp[i // 2] + 1)

    dp[i] = dp[i - 1] + 1 if dp[i] == 0 else min(dp[i], dp[i - 1] + 1)

print(dp[X])