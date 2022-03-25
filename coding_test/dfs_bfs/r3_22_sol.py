from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    fx, fy, sx, sy = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    # 상하좌우
    for i in range(4):
        nfx, nfy, nsx, nsy = fx + d[i][0], fy + d[i][1], sx + d[i][0], sy + d[i][1]
        if board[nfx][nfy] == 0 and board[nsx][nsy] == 0:
            next_pos.append({(nfx, nfy), (nsx, nsy)})

    #수평 or 수직
    if fx == sx:
        for i in [-1, 1]:
            if board[fx + i][fy] == 0 and board[sx + i][sy] == 0:
                next_pos.append({(fx, fy), (fx + i, fy)})
                next_pos.append({(sx, sy), (sx + i, sy)})
    elif fy == sy:
        for i in [-1, 1]:
            if board[fx][fy + i] == 0 and board[sx][sy + i] == 0:
                next_pos.append({(fx, fy), (fx, fy + i)})
                next_pos.append({(sx, sy), (sx, sy + i)})
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0