import sys
from collections import deque
input = sys.stdin.readline


def find_parent(node):
    x, y = node
    if parent[x][y] != node:
        parent[x][y] = find_parent(parent[x][y])
    return parent[x][y]


def union_parent(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    
    if pa != pb:
        ax, ay = pa
        parent[ax][ay] = pb
        
        
def range_checker(x, y):
    if 0 <= x < R and 0 <= y < C:
        return True
    return False


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def union():
    while to_union:
        pos = to_union.popleft()
        x, y = pos
        for d in direc:
            nx, ny = x + d[0], y + d[1]
            if range_checker(nx, ny):
                if lake[nx][ny] == '.': # 같은 물이면
                    union_parent((x, y), (nx, ny))
                else: # 빙하면
                    if not visited[nx][ny]: # 중복 녹이기 방지
                        to_water.append((nx, ny))
                visited[nx][ny] = True


def melt():
    while to_water:
        pos = to_water.popleft()
        x, y = pos
        lake[x][y] = '.' # 녹이기
        to_union.append((x, y))



R, C = map(int, input().split())
parent = [[(i, j) for j in range(C)] for i in range(R)]
visited = [[False] * C for _ in range(R)]
lake = [list(input()) for _ in range(R)]
L = []
for i in range(R):
    for j in range(C):
        if lake[i][j] == 'L':
            L.append((i, j))


to_union, to_water = deque(), deque()
    
day = 0
while True:
    union()
    if find_parent(L[0]) == find_parent(L[1]):
        break
    melt()
    day += 1
print(day)