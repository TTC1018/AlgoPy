from collections import deque


N = int(input())

home = []
for i in range(N):
    home.append(list(map(int, input())))

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited = [[-1] * N for _ in range(N)]

q = deque()

while q:
