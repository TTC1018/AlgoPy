N = int(input())
dp = [0] * (N + 1)

if N >= 10:
    dp[10] = 1 # 9876543210


print(dp[N])