# 가장 긴 증가 수열 (LIS)
# https://jainn.tistory.com/90

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
sequence = [0]
for a in A:
    if sequence[-1] < a: # 증가수열 충족하면
        sequence.append(a) # 그대로 이어줌
    else:
        loc = bisect_left(sequence, a)
        sequence[loc] = a 
sequence.pop(0)
print(len(sequence))