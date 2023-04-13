import sys
input = sys.stdin.readline

N, D = map(int, input().split())
R = [tuple(map(int, input().split())) for _ in range(N)]
dp = [10000] * (D + 1)

dp[0] = 0
for i in range(1, D + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    for s, e, c in R:
        if e == i:
            dp[i] = min(dp[i], dp[s] + c)
print(dp[D])