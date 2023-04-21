import sys
input = sys.stdin.readline


dp = [1] * (100000 + 1)
dp[1] = 1 # 1
dp[2] = 2 # 1+1, 2
dp[3] = 2 # 1+1+1, 3
dp[4] = 3
dp[5] = 3
dp[6] = 6

for i in range(7, 100000 + 1):
    dp[i] = (dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009

for _ in range(int(input())):
    print(dp[int(input())])