from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < 12 and 0 <= y < 6


def explode():
    global chain


    d_flag = False
    q = deque()
    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] != '.':
                q.append((i, j))
                color = field[i][j]
                visited = [[False] * 6 for _ in range(12)]
                visited[i][j] = True
                target = [(i, j)]
                while q:
                    x, y = q.popleft()

                    for d in direc:
                        nx, ny = x + d[0], y + d[1]
                        if in_range(nx, ny) and field[nx][ny] == color:
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                target.append((nx, ny))

                if len(target) >= 4:
                    for x, y in target:
                        field[x][y] = '.'
                    d_flag = True

    if d_flag:
        chain += 1
        drop()


def drop():
    for j in range(6):
        for i in range(10, -1, -1):
            if field[i][j] != '.':
                x = i
                while x < 11 and field[x + 1][j] == '.':
                    x += 1
                field[i][j], field[x][j] = '.', field[i][j]
    explode()



direc = [(-1, 0), (0, 1), (0, -1), (1, 0)]
field = [list(input().rstrip()) for _ in range(12)]

chain = 0
explode()
print(chain)