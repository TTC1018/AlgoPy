A, B = input(), input()
a_len, b_len = len(A), len(B)

dp = [0] * max(a_len, b_len)
dp[0] = 0 if A[0] == B[0] else 1

for i in range(1, len(dp)):
    pass