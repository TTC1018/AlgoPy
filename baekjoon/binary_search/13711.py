from bisect import bisect_left
import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB = [B.index(a) for a in A] # A의 원소가 B의 어느 위치에 있는지 기록

sequence = [-1]
for i in range(N):
    if sequence[-1] < AB[i]:
        sequence.append(AB[i])
    else:
        idx = bisect_left(sequence, AB[i])
        sequence[idx] = AB[i]
sequence.pop(0)

print(len(sequence))