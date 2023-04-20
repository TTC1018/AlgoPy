import sys
input = sys.stdin.readline

dp = [[0] * (9 + 1) for _ in range(64 + 1)] # x로 끝나는 n자리 수의 가짓수
for i in range(9 + 1):
    dp[1][i] = 1

for i in range(2, 64 + 1):
    for j in range(9 + 1):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

for _ in range(int(input())):
    print(sum(dp[int(input())]))