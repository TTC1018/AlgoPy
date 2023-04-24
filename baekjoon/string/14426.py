import sys
input = sys.stdin.readline


N, M = map(int, input().split())
S = sorted(input().rstrip() for _ in range(N))
P = [input().rstrip() for _ in range(M)]

answer = 0
for p in P:
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2

        if p < S[mid]:
            right = mid - 1
        elif p > S[mid]:
            left = mid + 1

        if p == S[mid][:len(p)]:
            answer += 1
            break
print(answer)
