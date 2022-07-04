import sys
input = sys.stdin.readline


N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
a_len = len(A)

answer = 0
for i in range(a_len - 1, -1, -1):
    if A[i] <= K:
        div, mod = divmod(K, A[i])
        answer += div
        K = mod
print(answer)