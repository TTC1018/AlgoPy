N = int(input())
t = list(map(int, input().split()))

dp = [0] * N
dp[0], dp[1] = t[0], max(t[0], t[1])

for i in range(2, N):
    dp[i] = max(dp[i-2] + t[i], dp[i-1])

print(dp[N-1])