A, B = input(), input()
a_len, b_len = len(A), len(B)

dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]
for i in range(a_len + 1):
    dp[i][0] = i
for i in range(b_len + 1):
    dp[0][i] = i

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            # dp[i][j - 1] + 1 => 문자 추가하기
            # dp[i - 1][j] + 1 => 문자 삭제하기
            # dp[i - 1][j - 1] + 1 => 문자 교체하기
            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
print(dp[a_len][b_len])