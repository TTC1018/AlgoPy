from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < 4 and 0 <= y < 4


def duplicate(new):
    for i in range(4):
        for j in range(4):
            board[i][j] += new[i][j]


def smell_is_gone():
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1


s_direc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def shark_move():
    global sx, sy

    q = deque()
    q.append((sx, sy, '', 0, 0, 0))

    cand = []
    while q:
        x, y, route, catch, visit, cnt = q.popleft()
        if cnt == 3:
            cand.append((catch, route))
            continue

        for d_idx, d in enumerate(s_direc):
            nx, ny = x + d[0], y + d[1]
            if in_range(nx, ny):
                bit = 1 << (nx * 4 + ny)
                if not (visit & bit):
                    q.append((nx, ny, route + str(d_idx + 1), catch + len(board[nx][ny]), visit | bit, cnt + 1))
                else:
                    q.append((nx, ny, route + str(d_idx + 1), catch, visit, cnt + 1))

    # 제외 물고기 큰 순, 사전 순으로 정렬
    cand.sort(key=lambda x: (-x[0], x[1]))
    for d in list(cand[0][1]):
        d = int(d) - 1
        sx, sy = sx + s_direc[d][0], sy + s_direc[d][1]
        if board[sx][sy]:
            smell[sx][sy] = 3
            board[sx][sy].clear()



def move():
    new_board = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            x, y = i, j
            for d in board[i][j]:
                for idx in range(d, d - 8, -1):
                    idx %= 8
                    nx, ny = x + direc[idx][0], y + direc[idx][1]
                    if in_range(nx, ny) and (nx, ny) != (sx, sy) and not smell[nx][ny]:
                        new_board[nx][ny].append(idx)
                        break
                else:
                    # 계속 회전해도 안 되면
                    new_board[x][y].append(d)
    return new_board


direc = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
board = [[[] for _ in range(4)] for _ in range(4)]

M, S = map(int, input().split())
for _ in range(M):
    fx, fy, d = map(int, input().split())
    fx -= 1
    fy -= 1
    d -= 1
    board[fx][fy].append(d)
sx, sy = map(int, input().split())
sx -= 1
sy -= 1

smell = [[0] * 4 for _ in range(4)]
for _ in range(S):
    board_cpy = board.copy()  # 복사
    board = move() # 물고기 이동
    shark_move() # 상어 이동
    smell_is_gone() # 냄새 제거
    duplicate(board_cpy) # 복사한 물고기 추가

answer = 0
for i in range(4):
    for j in range(4):
        answer += len(board[i][j])
print(answer)