import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

N, M = map(int, input().split())
rooms = []
vs = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    rooms.append(list(map(int, input().split())))
    for j in range(N):
        if rooms[i][j] == 2:
            vs.append((i, j, 0))


def check(room_map):
    for i in range(N):
        for j in range(N):
            if room_map[i][j] == 0:
                return False
    return True


def spread(points, room_map):
    visited = [[False] * N for _ in range(N)]
    temp_map = deepcopy(room_map)
    q = deque()

    q.extend(points)
    result = 0
    while q:
        r, c, cnt = q.popleft()
        visited[r][c] = True
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and temp_map[nr][nc] != 1:
                visited[nr][nc] = True
                if temp_map[nr][nc] == 0:
                    temp_map[nr][nc] = 2
                    result = cnt + 1
                q.append((nr, nc, cnt + 1))
    if check(temp_map):
        return result
    else:
        return -1


answer = sys.maxsize
for c in combinations(vs, M):
    result = spread(c, rooms)
    if result != -1:
        answer = min(answer, result)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)