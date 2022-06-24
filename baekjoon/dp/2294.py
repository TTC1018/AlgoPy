import sys
input = sys.stdin.readline


n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]

INF = int(1e9)
dp = [INF] * (max(k, max(c)) + 1)

dp[0] = 0
for cost in c:
    dp[cost] = 1

for num in range(1, k + 1):
    for cost in c:
        if num - cost > 0:
            dp[num] = min(dp[num], dp[num - cost] + 1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])