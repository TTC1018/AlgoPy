import sys
input = sys.stdin.readline


A, B, C = input().rstrip(), input().rstrip(), input().rstrip()
a_len, b_len, c_len = len(A), len(B), len(C)
dp = [[[0] * (c_len + 1) for _ in range(b_len + 1)] for _ in range(a_len + 1)]

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        for k in range(1, c_len + 1):
            if A[i - 1] == B[j - 1] == C[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
print(dp[a_len][b_len][c_len])