A, B = input(), input()
a_len, b_len = len(A), len(B)
dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]
for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1 # 같은 경우, 한 자리 적은 LCS 경우의 수에 1 더해서 갱신
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) # 다른 경우, A가 한자리 적거나 B가 한자리 적은 경우의 LCS 그대로 가져오기
print(dp[a_len][b_len])