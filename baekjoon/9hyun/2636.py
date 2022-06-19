from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < R and 0 <= y < C


direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
air_num = 0
def bfs(i, j):
    q = deque()
    q.append((i, j))
    area[i][j] = air_num

    while q:
        x, y = q.popleft()

        for d in direc:
            nx, ny = x + d[0], y + d[1]
            if in_range(nx, ny) and area[nx][ny] == -1:
                if not graph[nx][ny]:
                    area[nx][ny] = air_num
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    area[nx][ny] = air_num + 1

def melt():
    global melted

    removed = 0
    nxt = set()
    for i in range(R):
        for j in range(C):
            if area[i][j] == air_num + 1:
                area[i][j] = air_num
                graph[i][j] = air_num
                removed += 1

                for d in direc:
                    ni, nj = i + d[0], j + d[1]
                    if in_range(ni, nj):
                        if graph[ni][nj] == 1 and area[ni][nj] == -1:
                            nxt.add((ni, nj))

    for x, y in nxt:
        area[x][y] = air_num + 1

    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                return False

    melted = removed
    return True


R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]


time = 0
while True:
    time += 1

    area = [[-1] * C for _ in range(R)]
    bfs(0, 0)
    # 치즈 녹이기
    melted = 0
    if melt():
        print(time)
        print(melted)
        break