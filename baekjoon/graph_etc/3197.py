import sys
from collections import deque

input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < R and 0 <= y < C
direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def find_parent(node):
    x, y = node
    if parent[x][y] == node:
        return node
    parent[x][y] = find_parent(parent[x][y])
    return parent[x][y]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    
    ax, ay = pa
    bx, by = pb

    # 자식이 더 많은 쪽이 부모가 되도록 설정
    if p_cnt[ax][ay] > p_cnt[bx][by]:
        parent[bx][by] = pa
    elif p_cnt[ax][ay] < p_cnt[bx][by]:
        parent[ax][ay] = pb
    else:
        parent[bx][by] = pa
        p_cnt[ax][ay] += 1


def first_union():
    for i in range(R):
        for j in range(C):
            if not visited[i][j] and lake[i][j] == ".":
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    parent[x][y] = (i, j)
                    for d in direc:
                        nx, ny = x + d[0], y + d[1]
                        if in_range(nx, ny) and not visited[nx][ny]:
                            if lake[nx][ny] == ".":
                                q.append((nx, ny))
                            elif lake[nx][ny] == "X":
                                to_water.append((nx, ny))
                            visited[nx][ny] = True


def ice_to_water():
    global to_water
    
    nexts = deque()
    while to_water:
        x, y = to_water.popleft()
        lake[x][y] = "."
        for d in direc:
            nx, ny = x + d[0], y + d[1]
            if in_range(nx, ny):
                if not visited[nx][ny] and lake[nx][ny] == "X":
                    nexts.append((nx, ny))
                    visited[nx][ny] = True
                elif lake[nx][ny] == ".":
                    union_parent((nx, ny), (x, y))
    to_water = nexts


R, C = map(int, input().split())
lake = [list(input()) for _ in range(R)]
parent = [[(i, j) for j in range(C)] for i in range(R)]
p_cnt = [[0 for _ in range(C)] for _ in range(R)] # union 최적화를 위한 배열
visited = [[False] * C for _ in range(R)]
L = []
for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            L.append((i, j))
            lake[i][j] = "."
            if len(L) == 2:
                break

to_water = deque()
day = 0
first_union()
while find_parent(L[0]) != find_parent(L[1]):
    ice_to_water()
    day += 1
print(day)