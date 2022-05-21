A = input()
B = input()

a_len, b_len = len(A), len(B)
answer = 0
dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]
for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1 # 누적 DP 그래프를 사용하지 않고, 한자리 작은 A, B의 DP 값을 가져와서 1을 더한다
            answer = max(answer, dp[i][j])
print(answer)