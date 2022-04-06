N = int(input())
P = list(map(int, input().split()))
M = int(input())

dp = [-5001] * (M + 1)
for i in range(N - 1, -1, -1): # 번호 역순으로
    target = P[i]
    for j in range(target, M + 1):
        dp[j] = max(dp[j], dp[j-target]*10 + i, i)
print(dp[M])