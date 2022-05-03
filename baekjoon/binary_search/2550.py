from bisect import bisect_left
import sys
input = sys.stdin.readline


N = int(input())
S = list(map(int, input().split()))
E = list(map(int, input().split()))

A = []
for i in range(N):
    A.append(E.index(S[i]) + 1)

sequence = [-1]
s_idx = [0] * N
max_idx = 0
for i in range(N):
    if sequence[-1] < A[i]:
        sequence.append(A[i])
        s_idx[i] = len(sequence) - 1
        max_idx = s_idx[i]
    else:
        s_idx[i] = bisect_left(sequence, A[i])
        sequence[s_idx[i]] = A[i]
sequence.pop(0)

answer = []
for i in range(N - 1, -1, -1):
    if s_idx[i] == max_idx:
        answer.append(S[i])
        max_idx -= 1
answer.reverse()
answer.sort()
print(len(answer))
print(*answer)