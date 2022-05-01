import sys
input = sys.stdin.readline


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

dp[0] = costs[0]
for i in range(1, N):
    for j in range(3):
        dp[i][j] = min([n for idx, n in enumerate(dp[i - 1]) if idx != j]) + costs[i][j]
print(min(dp[N - 1]))