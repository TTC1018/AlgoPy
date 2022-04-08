# 3 X N 크기의 벽을
# 2X1, 1X2로 채우기
N = int(input())
dp = [1, 0, 3] + [0] * (N - 2)
for i in range(1, N + 1, 2):
    dp[i] = 0
for i in range(4, N + 1, 2):
    for j in range(i - 2, -1, -2):
        if j == i - 2:
            dp[i] += (dp[2] * dp[j])
        else:
            dp[i] += (dp[j] * 2)
print(dp[N])