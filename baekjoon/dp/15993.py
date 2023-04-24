import sys
input = sys.stdin.readline
MOD = 1000000009

dp = [[0] * 2 for _ in range(100000 + 1)]

dp[1][0] = 1
dp[2][0] = 1; dp[2][1] = 1
dp[3][0] = 2; dp[3][1] = 2
for num in range(4, 100000 + 1):
    dp[num][0] += (dp[num - 1][1] + dp[num - 2][1] + dp[num - 3][1]) % MOD
    dp[num][1] += (dp[num - 1][0] + dp[num - 2][0] + dp[num - 3][0]) % MOD

for _ in range(int(input())):
    print(*dp[int(input())])