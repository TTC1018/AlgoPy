N = int(input())
P = list(map(int, input().split()))

dp = [0] * (N + 1)
# 초기화
for i in range(1, N + 1):
    dp[i] = P[i - 1]

for i in range(2, N + 1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[N])