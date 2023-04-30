import sys
input = sys.stdin.readline


N, M = map(int, input().split())
A = list(map(int, input().split()))
P = A[:]
for i in range(1, N):
    P[i] += P[i - 1]

max_val = 0
left, right = 0, 0
while left < N and right < N:
    if left == right:
        if A[left] <= M:
            max_val = max(max_val, A[left])
            right += 1
        else:
            left += 1
            right += 1
    elif left == 0 and P[right] <= M:
        max_val = max(max_val, P[right])
        right += 1
    elif left > 0 and P[right] - P[left - 1] <= M:
        max_val = max(max_val, P[right] - P[left - 1])
        right += 1
    else:
        left += 1
print(max_val)