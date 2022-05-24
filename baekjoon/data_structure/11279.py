from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
q = []
for _ in range(N):
    data = int(input())

    if data == 0:
        if not q:
            print(0)
        else:
            print(-heappop(q))
    else:
        heappush(q, -data)