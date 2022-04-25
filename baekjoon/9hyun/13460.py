from copy import deepcopy


def to_left(board_arg):
    rx, ry = locs[0]
    bx, by = locs[1]
    
    if ry < by: # 빨간 구슬이 파란 구슬보다 왼쪽
        #빨간 구슬부터 이동
        for ny in range(ry - 1, -1, -1):
            if board_arg[rx][ny] == 'O':
                board_arg[rx][ry] = '.'
                finished[0] = True
                ry = ny
                break
            elif board_arg[rx][ny] == '.':
                locs[0] = (rx, ny)
                board_arg[rx][ry], board_arg[rx][ny] = '.', 'R'
                ry = ny
            elif board_arg[rx][ny] == '#':
                break
        for ny in range(by - 1, -1, -1):
            if board_arg[bx][ny] == 'O':
                board_arg[bx][by] = '.'
                finished[1] = True
                by = ny
                break
            elif board_arg[bx][ny] == '.':
                locs[1] = (bx, ny)
                board_arg[bx][by], board_arg[bx][ny] = '.', 'B'
                by = ny
            else: # 빨간 구슬이 있거나 벽일 때
                break
    else: #파란 구슬이 빨간 구슬보다 왼쪽
        #파란 구슬부터 이동
        for ny in range(by - 1, -1, -1):
            if board_arg[bx][ny] == 'O':
                board_arg[bx][by] = '.'
                finished[1] = True
                by = ny
                break
            elif board_arg[bx][ny] == '.':
                locs[1] = (bx, ny)
                board_arg[bx][by], board_arg[bx][ny] = '.', 'B'
                by = ny
            elif board_arg[bx][ny] == '#':
                break
        for ny in range(ry - 1, -1, -1):
            if board_arg[rx][ny] == 'O':
                board_arg[rx][ry] = '.'
                finished[0] = True
                ry = ny
                break
            elif board_arg[rx][ny] == '.':
                board_arg[rx][ry], board_arg[rx][ny] = '.', 'R'
                ry = ny
                locs[0] = (rx, ny)
            else:
                break
    
    locs[0] = (rx, ry)
    locs[1] = (bx, by)
    return board_arg
            
            
def to_right(board_arg):
    rx, ry = locs[0]
    bx, by = locs[1]
    
    if ry < by: # 파란 구슬이 빨간 구슬보다 오른쪽
        #파란 구슬부터 이동
        for ny in range(by + 1, M):
            if board_arg[bx][ny] == 'O':
                finished[1] = True
                by = ny
                break
            elif board_arg[bx][ny] == '.':
                locs[1] = (bx, ny)
                board_arg[bx][by], board_arg[bx][ny] = '.', 'B'
                by = ny
            elif board_arg[bx][ny] == '#':
                break
        for ny in range(ry + 1, M):
            if board_arg[rx][ny] == 'O':
                finished[0] = True
                ry = ny
                break
            elif board_arg[rx][ny] == '.':
                locs[0] = (rx, ny)
                board_arg[rx][ry], board_arg[rx][ny] = '.', 'R'
                ry = ny
            else:
                break   
    else: # 빨간 구슬이 파란 구슬보다 오른쪽
        #빨간 구슬부터 이동
        for ny in range(ry + 1, M):
            if board_arg[rx][ny] == 'O':
                finished[0] = True
                ry = ny
                break
            elif board_arg[rx][ny] == '.':
                locs[0] = (rx, ny)
                board_arg[rx][ry], board_arg[rx][ny] = '.', 'R'
                ry = ny
            elif board_arg[rx][ny] == '#':
                break
        for ny in range(by + 1, M):
            if board_arg[bx][ny] == 'O':
                finished[1] = True
                by = ny
                break
            elif board_arg[bx][ny] == '.':
                locs[1] = (bx, ny)
                board_arg[bx][by], board_arg[bx][ny] = '.', 'B'
                by = ny
            else:
                break
    locs[0] = (rx, ry)
    locs[1] = (bx, by)
    return board_arg
        

def to_up(board_arg):
    rx, ry = locs[0]
    bx, by = locs[1]
    
    if rx < bx: # 빨간 구슬이 파란 구슬보다 위쪽
        #빨간 구슬부터 이동
        for nx in range(rx - 1, -1, -1):
            if board_arg[nx][ry] == 'O':
                board_arg[nx][ry] = '.'
                finished[0] = True
                rx = nx
                break
            elif board_arg[nx][ry] == '.':
                locs[0] = (nx, ry)
                board_arg[rx][ry], board_arg[nx][ry] = '.', 'R'
                rx = nx
            elif board_arg[nx][ry] == '#':
                break
        for nx in range(bx - 1, -1, -1):
            if board_arg[nx][by] == 'O':
                board_arg[bx][by] = '.'
                finished[1] = True
                bx = nx
                break
            elif board_arg[nx][by] == '.':
                locs[1] = (nx, by)
                board_arg[bx][by], board_arg[nx][by] = '.', 'B'
                bx = nx
            else: # 빨간 구슬이 있거나 벽일 때
                break
    else: #파란 구슬이 빨간 구슬보다 위쪽
        #파란 구슬부터 이동
        for nx in range(bx - 1, -1, -1):
            if board_arg[nx][by] == 'O':
                board_arg[bx][by] = '.'
                finished[1] = True
                bx = nx
                break
            elif board_arg[nx][by] == '.':
                locs[1] = (nx, by)
                board_arg[bx][by], board_arg[nx][by] = '.', 'B'
                bx = nx
            elif board_arg[nx][by] == '#':
                break
        for nx in range(rx - 1, -1, -1):
            if board_arg[nx][ry] == 'O':
                board_arg[rx][ry] = '.'
                finished[0] = True
                rx = nx
                break
            elif board_arg[nx][ry] == '.':
                board_arg[rx][ry], board_arg[nx][ry] = '.', 'R'
                rx = nx
                locs[0] = (nx, ry)
            else:
                break
            
    locs[0] = (rx, ry)
    locs[1] = (bx, by)
    return board_arg


def to_down(board_arg):
    rx, ry = locs[0]
    bx, by = locs[1]
    
    if rx > bx: # 빨간 구슬이 파란 구슬보다 아래쪽
        #빨간 구슬부터 이동
        for nx in range(rx + 1, N):
            if board_arg[nx][ry] == 'O':
                board_arg[nx][ry] = '.'
                finished[0] = True
                rx = nx
                break
            elif board_arg[nx][ry] == '.':
                locs[0] = (nx, ry)
                board_arg[rx][ry], board_arg[nx][ry] = '.', 'R'
                rx = nx
            elif board_arg[nx][ry] == '#':
                break
        for nx in range(bx + 1, N):
            if board_arg[nx][by] == 'O':
                board_arg[bx][by] = '.'
                finished[1] = True
                bx = nx
                break
            elif board_arg[nx][by] == '.':
                locs[1] = (nx, by)
                board_arg[bx][by], board_arg[nx][by] = '.', 'B'
                bx = nx
            else: # 빨간 구슬이 있거나 벽일 때
                break
    else: #파란 구슬이 빨간 구슬보다 아래쪽
        #파란 구슬부터 이동
        for nx in range(bx + 1, N):
            if board_arg[nx][by] == 'O':
                board_arg[bx][by] = '.'
                finished[1] = True
                bx = nx
                break
            elif board_arg[nx][by] == '.':
                locs[1] = (nx, by)
                board_arg[bx][by], board_arg[nx][by] = '.', 'B'
                bx = nx
            elif board_arg[nx][by] == '#':
                break
        for nx in range(rx + 1, N):
            if board_arg[nx][ry] == 'O':
                board_arg[rx][ry] = '.'
                finished[0] = True
                rx = nx
                break
            elif board_arg[nx][ry] == '.':
                board_arg[rx][ry], board_arg[nx][ry] = '.', 'R'
                rx = nx
                locs[0] = (nx, ry)
            else:
                break
    locs[0] = (rx, ry)
    locs[1] = (bx, by)
    return board_arg
    
        

def dfs(board_arg, count):
    global answer, finished, locs
    if finished[1]:
        return    
    if count > 10:
        return
    if finished[0] and not finished[1]:
        answer = min(answer, count)
        return
    
    locs_save = locs[:]
    finished_save = finished[:]
    for op in ops:
        result = op(deepcopy(board_arg))
        print(result)
        if not rvisit[locs[0][0]][locs[0][1]] or not bvisit[locs[1][0]][locs[1][1]]:
            rvisit[locs[0][0]][locs[0][1]] = True
            bvisit[locs[1][0]][locs[1][1]] = True
            dfs(result, count + 1)
        finished = finished_save
        locs = locs_save

INF = int(1e9)
N, M = map(int, input().split())
locs = [(0, 0), (0, 0)]
finished = [False, False]
board = []
for i in range(N):
    data = list(input())
    for j in range(M):
        if data[j] == 'R':
            locs[0] = (i, j)
        elif data[j] == 'B':
            locs[1] = (i, j)
    board.append(data)

ops = [to_up, to_right, to_down, to_left]

answer = INF
rvisit = [[False] * M for _ in range(N)]
bvisit = [[False] * M for _ in range(N)]
rvisit[locs[0][0]][locs[0][1]] = True
bvisit[locs[1][0]][locs[1][1]] = True
dfs(board, 0)
if answer != INF:
    print(answer)
else:
    print(-1)