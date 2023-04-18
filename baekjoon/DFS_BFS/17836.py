from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


N, M, T = map(int, input().split())
board = list(map(int, input().split()))

q = deque([(0, 0, 0, False)]) # x, y, 시간, 그람유무
while q:
    x, y, t, g = q.popleft()