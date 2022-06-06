from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = deepcopy(triangle)

for i in range(1, n):
    dp[i][0] += dp[i - 1][0]
    dp[i][i] += dp[i - 1][i - 1]
    for j in range(1, i):
        dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[n - 1]))