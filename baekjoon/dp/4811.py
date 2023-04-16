import sys
input = sys.stdin.readline

dp = [[0] * (30 + 1) for _ in range(30 + 1)]
for w in range(1, 30 + 1):
    dp[w][0] = 1
# W
# WW
# WWW
# WWWW...


# 예) dp[2][1] => WHW, WWH = dp[1][1] + dp[2][0]
# 예) dp[3][1] => WHWW, WWHW, WWWH => dp[2][1] + dp[3][0]
# W나 H가 하나 작은 경우에 W or H를 붙여주는 것
for w in range(1, 30 + 1):
    for h in range(1, w + 1):
        dp[w][h] = dp[w - 1][h] + dp[w][h - 1]

while True:
    N = int(input())
    if N == 0:
        break
    print(max(dp[N]))