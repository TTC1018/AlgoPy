N = int(input())
P = list(map(int, input().split()))
M = int(input())

# 가장 큰 수를 고르는 게 이득
# 그러나 자릿 수가 늘어나는 게 큰 수 하나보다 나음
dp = [''] * (M + 1)
for i in range(N):
    dp[P[i]] += str(i)
print(dp)