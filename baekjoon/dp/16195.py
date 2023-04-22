import sys
input = sys.stdin.readline
MOD = 1000000009


dp = [[0] * (1000 + 1) for _ in range(1000 + 1)]
dp[1][1] = 1
dp[2][1] = 1; dp[2][2] = 1
dp[3][1] = 1
for num in range(3, 1000 + 1):
    for cnt in range(2, num + 1):
        dp[num][cnt] += (dp[num - 1][cnt - 1] + dp[num - 2][cnt - 1] + dp[num - 3][cnt - 1]) % MOD


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(sum(dp[n][:m+1]) % MOD)