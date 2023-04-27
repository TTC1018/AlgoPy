import sys
input = sys.stdin.readline
MOD = 1000007


w, h = map(int, input().split())
tx, ty = map(lambda x: int(x) - 1, input().split())
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for i in range(w):
    dp[0][i] = 1
for i in range(h):
    dp[i][0] = 1
for i in range(1, ty + 1):
    for j in range(1, tx + 1):
        dp[i][j] += (dp[i][j - 1] + dp[i - 1][j]) % MOD


for i in range(tx + 1, w):
    dp[ty][i] = dp[ty][tx]
for i in range(ty + 1, h):
    dp[i][tx] = dp[ty][tx]
for i in range(ty + 1, h):
    for j in range(tx + 1, w):
        dp[i][j] += (dp[i][j - 1] + dp[i - 1][j]) % MOD
print(dp[h - 1][w - 1])