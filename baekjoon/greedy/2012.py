import sys
input = sys.stdin.readline

N = int(input())
expect = [0] + [int(input()) for _ in range(N)]
expect.sort()
answer = 0
for i in range(1, N + 1):
    if expect[i] != i:
        answer += abs(i - expect[i])
print(answer)