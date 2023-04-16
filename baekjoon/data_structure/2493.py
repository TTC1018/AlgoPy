import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
stack = []

answer = [0] * N
for i in range(N - 1, -1, -1):
    while stack and stack[-1][1] <= T[i]:
        idx, height = stack.pop()
        answer[idx] = i + 1
    stack.append((i, T[i]))
print(*answer)
