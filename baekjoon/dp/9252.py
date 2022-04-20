A, B = input(), input()
a_len, b_len = len(A), len(B)
dp = [[(0, '') for _ in range(b_len + 1)] for _ in range(a_len + 1)]

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = (dp[i - 1][j - 1][0] + 1, dp[i - 1][j - 1][1] + A[i - 1])
        else:
            if dp[i - 1][j][0] > dp[i][j - 1][0]:
                dp[i][j] = (dp[i - 1][j][0], dp[i - 1][j][1])
            else:
                dp[i][j] = (dp[i][j - 1][0], dp[i][j - 1][1])
a1, a2 = dp[a_len][b_len]
print(a1)
print(a2)