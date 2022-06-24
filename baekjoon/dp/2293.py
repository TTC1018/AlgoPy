import sys
input = sys.stdin.readline

n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]

dp = [0] * (max(max(c), k) + 1)
dp[0] = 1
for cost in c:
    for num in range(1, k + 1):
        if num - cost >= 0:
            dp[num] += dp[num - cost]
print(dp[k])