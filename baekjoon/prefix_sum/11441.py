import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i]

for _ in range(int(input())):
    i, j = map(int, input().split())
    print(S[j] - S[i - 1])