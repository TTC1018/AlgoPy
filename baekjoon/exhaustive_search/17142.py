from itertools import combinations
from copy import deepcopy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def spread(r_var, row, col, cnt):
    for i in range(4):
        nr = row + dx[i]
        nc = col + dy[i]
        if 0 <= nr < N and 0 <= nc < N:
            if r_var[nr][nc] == 0 or r_var[nr][nc] <= cnt - 1:
                r_var[nr][nc] = cnt - 1
                spread(r_var, nr, nc, cnt - 1)


def check(room_map):
    for r in room_map:
        if 0 in r:
            return False
    return True


N, M = map(int, input().split())
rooms = []
vs = []

for i in range(N):
    rooms.append(list(map(int, input().split())))
    for j in range(N):
        if rooms[i][j] == 2:
            vs.append((i, j))


answer = -(N + 1)
q = deque()
for c in combinations(vs, M):
    q.append(c)

while q:
    temp_rooms = deepcopy(rooms)
    for virus in q.popleft():
        row, col = virus
        spread(temp_rooms, row, col, 0)
    if check(temp_rooms):
        c_answer = min(temp_rooms[0])
        for i in range(1, N):
            c_answer = min(c_answer, min(temp_rooms[i]))
        answer = max(answer, c_answer)

if answer == -(N + 1):
    print(-1)
elif answer == 1 or answer == 2:
    print(0)
else:
    print(abs(answer))