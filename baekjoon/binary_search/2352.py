from bisect import bisect_left
import sys
input = sys.stdin.readline


n = int(input())
p = list(map(int, input().split()))

sequence = [-1]
for i in range(n):
    if sequence[-1] < p[i]:
        sequence.append(p[i])
    else:
        idx = bisect_left(sequence, p[i])
        sequence[idx] = p[i]
sequence.pop(0)

print(len(sequence))