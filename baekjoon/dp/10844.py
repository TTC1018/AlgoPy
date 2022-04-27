import sys
input = sys.stdin.readline


N = int(input())
dp = [[1] * 10 for _ in range(N + 1)] # 길이가 N일 때 마지막 숫자가 X로 끝나면 갖는 계단수 개수
dp[1][0] = 0 # 0은 혼자 있는 거 불가능

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1] # 0으로 끝나면 바로 앞자리 1만 가능
    for j in range(1, 8 + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 10**9
    dp[i][9] = dp[i - 1][8] # 9로 끝나면 바로 앞자리 8만 가능
print(sum(dp[N]) % 10**9)