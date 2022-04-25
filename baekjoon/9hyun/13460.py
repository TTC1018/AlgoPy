from collections import deque
import sys
input = sys.stdin.readline


def roll(x, y, dx, dy):
    rolled = 0 # 구른 횟수
    nx, ny = x, y
    while board[nx + dx][ny + dy] != '#' and board[nx][ny] != 'O': # 벽을 만나거나 구멍에 도착할 때까지 구르기
        nx += dx
        ny += dy
        rolled += 1
    return nx, ny, rolled


direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int,input().split())
visited = dict()
board = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            dest = (i, j)

q = deque()
q.append([red, blue, 0])
while q:
    r, b, count = q.popleft()
    rx, ry = r
    bx, by = b
    
    if count >= 10:
        break
    
    for d in direc:
        nrx, nry, r_count = roll(rx, ry, d[0], d[1])
        nbx, nby, b_count = roll(bx, by, d[0], d[1])
        if board[nbx][nby] != 'O': # 파란 구슬은 못 나갔을 때만
            if (nrx, nry) == dest: # 빨간 구슬은 나감
                print(count + 1)
                sys.exit()
            if (nrx, nry) == (nbx, nby): # 구슬이 같은 위치일 때
                if r_count > b_count: # 빨간 구슬이 더 먼곳에서 왔을 때
                    nrx -= d[0]
                    nry -= d[1]
                else: # 파란 구슬이 더 멀리서 왔을 때 무르기
                    nbx -= d[0]
                    nby -= d[1]
            
            if ((nrx, nry), (nbx, nby)) in visited:
                continue
            else:
                visited[((nrx, nry), (nbx, nby))] = True
                q.append([(nrx, nry), (nbx, nby), count + 1]) 
print(-1)