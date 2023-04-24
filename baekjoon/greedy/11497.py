from collections import deque
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    L = sorted(map(int, input().split()))

    q = deque()
    left, right = N - 2, N - 1
    if N % 2 != 0:
        q.append(L[right])
        left -= 1
        right -= 1

    while left >= 0:
        q.appendleft(L[left])
        q.append(L[right])
        left -= 2
        right -= 2

    print(max(abs(q[0] - q[-1]), max([abs(q[i] - q[i - 1]) for i in range(1, N)])))
