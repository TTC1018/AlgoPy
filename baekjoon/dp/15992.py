import sys
input = sys.stdin.readline
MOD = 1000000009

dp = [[0] * (1000 + 1) for i in range(1000 + 1)]
for num in range(1, 1000 + 1):
    dp[num][num] = 1
for num in range(1, 3 + 1):
    dp[num][1] = 1
dp[3][2] = 2
for num in range(4, 1000 + 1):
    for cnt in range(2, num):
        dp[num][cnt] += (dp[num - 1][cnt - 1] + dp[num - 2][cnt - 1] + dp[num - 3][cnt - 1]) % MOD

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(dp[n][m])