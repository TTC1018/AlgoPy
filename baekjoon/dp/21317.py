import sys
input = sys.stdin.readline


N = int(input())
E = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N - 1)]
K = int(input())

dp = [[int(1e9)] * 2 for _ in range(max(4, N) + 1)]
dp[1][0] = 0
if N > 1:
    dp[2][0] = E[1][0]
if N > 2:
    dp[3][0] = min(E[1][1], dp[2][0] + E[2][0])
if N > 3:
    dp[4][0] = min(dp[2][0] + E[2][1], dp[3][0] + E[3][0])
    dp[4][1] = min(dp[3][1] + E[3][0], K)

for stone in range(4, N + 1):
    dp[stone][0] = min(dp[stone][0], dp[stone - 1][0] + E[stone - 1][0], dp[stone - 2][0] + E[stone - 2][1])
    dp[stone][1] = min(dp[stone][1], dp[stone - 1][1] + E[stone - 1][0], dp[stone - 2][1] + E[stone - 2][1], dp[stone - 3][0] + K)
print(min(dp[N]))