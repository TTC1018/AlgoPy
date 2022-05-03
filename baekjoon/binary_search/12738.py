from bisect import bisect_left
import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

sequence = [-10**9 - 1]
for i in range(N):
    if sequence[-1] < A[i]:
        sequence.append(A[i])
    else:
        idx = bisect_left(sequence, A[i])
        sequence[idx] = A[i]
sequence.pop(0)

print(len(sequence))