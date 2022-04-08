# 3 X N 크기의 벽을
# 2X1, 1X2로 채우기
# 각 경우마다 생기는 특이한 모양 2가지가 핵심
N = int(input())
dp = [1, 0, 3] + [0] * (N - 2)

# 홀수 = 불가능
for i in range(1, N + 1, 2):
    dp[i] = 0
# dp[i] = dp[i-2]*3가지 + dp[i-4]*dp[i-4]특이케이스 + ... + dp[i]특이케이스
# dp[i] = dp[i-2]*dp[2] + dp[i-4]*2  + ... + 2
for i in range(4, N + 1, 2):
    dp[i] += (dp[2] * dp[i - 2])
    for j in range(i - 4, -1, -2):
        dp[i] += (dp[j] * 2)
print(dp[N])