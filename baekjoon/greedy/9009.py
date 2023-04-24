from collections import deque
from bisect import bisect_left
import sys
input = sys.stdin.readline

d = {0:0, 1:1}
def fibo(num):
    if num in d:
        return d[num]

    d[num] = fibo(num - 1) + fibo(num - 2)
    return d[num]

fibo(45)
F = list(d.values())
for _ in range(int(input())):
    n = int(input())
    q = deque()
    while n > 0:
        b_idx = bisect_left(F, n)

        if F[b_idx] == n:
            q.appendleft(F[b_idx])
            n = 0
        else:
            q.appendleft(F[b_idx - 1])
        n -= q[0]
    print(*q)