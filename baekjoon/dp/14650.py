import sys
input = sys.stdin.readline


N = int(input())
dp = [[0] * (N * 2 + 1) for _ in range(N + 1)]
dp[1][1] = 1
dp[1][2] = 1

nums = list(range(2 + 1))
for n in range(2, N + 1):
    for sum_val in range(1, n * 2 + 1):
        for num in nums:
            dp[n][sum_val] += dp[n - 1][sum_val - num]
print(sum([dp[N][num] for num in range(3, N * 2 + 1, 3)]))
