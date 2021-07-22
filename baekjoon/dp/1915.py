n, m = [int(''.join(n)) for n in input().split(' ')]
nums = []
dp = []
for i in range(n):
    nums.append([int(n) for n in input()])
    dp.append([0] * m)

answer = 0
# 초기화
for i in range(n):
    if nums[i][0] == 1:
        dp[i][0] = 1
        answer = 1
    else:
        dp[i][0] = 0
for i in range(m):
    if nums[0][i] == 1:
        dp[0][i] = 1
        answer = 1
    else:
        dp[0][i] = 0

# DP
if n > 1 and m > 1:
    for i in range(1, n):
        for j in range(1, m):
            if nums[i][j] != 0:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1], i, j) + 1
                answer = max(answer, dp[i][j])

print(answer ** 2)
