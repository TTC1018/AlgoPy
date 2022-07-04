import sys
input = sys.stdin.readline


N, K = map(int, input().split())
MOD = 10**9

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][1] = 1 # 숫자 한개로 i를 만들 수 있는 경우의 수

for i in range(N + 1):
    for j in range(2, K + 1):
        for k in range(j):
            # 숫자 j개로 i를 만들 수 있는 경우의 수 = 숫자 1..j 개로 i - 1을 만들 수 있는 경우의 수의 합
            # (여기에 1만 더해주면 되기 때문)
            dp[i][j] += dp[i - 1][j - k]
            dp[i][j] %= MOD
print(dp[N][K])