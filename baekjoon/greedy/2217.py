import sys
input = sys.stdin.readline

N = int(input())
W = [int(input()) for _ in range(N)]
W.sort()

max_val = 0
for i in range(1, N + 1):
    max_val = max(max_val, W[-i] * i)
print(max_val)