import sys
input = sys.stdin.readline

A, B = input().rstrip(), input().rstrip()

A = [ord(a) for a in A]
B = [ord(b) for b in B]

a_len, b_len = len(A), len(B)
DP = [[0] * (b_len + 1) for _ in range(a_len + 1)]

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if A[i - 1] == B[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(DP[a_len][b_len])