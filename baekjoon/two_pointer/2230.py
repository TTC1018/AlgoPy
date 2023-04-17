import sys
input = sys.stdin.readline


N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])

answer = int(1e10)
left, right = 0, 0
while left < N and right < N:
    diff = A[right] - A[left]
    if diff >= M:
        left += 1
        answer = min(answer, diff)
    else:
        right += 1
print(answer)