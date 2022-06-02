from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
HW = [tuple(map(int, input().split())) for _ in range(N)]
HW.sort(key=lambda x: x[0])

q = []
for d, w in HW:
    heappush(q, w)
    if len(q) > d:
        heappop(q)
print(sum(q))