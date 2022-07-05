from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
d = defaultdict(int)
for _ in range(N):
    d[input().rstrip()] += 1
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(d[0][0])
