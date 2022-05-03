from bisect import bisect_left
import sys
input = sys.stdin.readline


N = int(input())
B = list(map(int, input().split()))

sequence = [-1]
for i in range(N):
    if sequence[-1] < B[i]:
        sequence.append(B[i])
    else:
        sequence[bisect_left(sequence, B[i])] = B[i]
sequence.pop(0)

print(N - len(sequence))