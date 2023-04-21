import sys
input = sys.stdin.readline
INF = int(1e9)
MOD = 1000000007

D = int(input())
dp = [[0] * 8 for _ in range(D + 1)]
graph = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 4],
    [1, 2, 4, 5],
    [2, 3, 5, 6],
    [3, 4, 7],
    [4, 7],
    [5, 6]
]

dp[0][0] = 1
for d in range(1, D + 1):
    for l in range(8):
        for prev in graph[l]:
            dp[d][l] += dp[d - 1][prev]
            dp[d][l] %= MOD
print(dp[D][0])
