import sys
from collections import defaultdict
in_range = lambda x, y: 0 <= x < N and 0 <= y < N
input = sys.stdin.readline


def move():
    for n in chess_piece:
        x, y, d = chess_piece[n]
        nx, ny = x + direc[d][0], y + direc[d][1]

        # 범위 밖 or 파란칸
        if not in_range(nx, ny) or board[nx][ny] == blue:
            d = direc.index((-direc[d][0], -direc[d][1]))
            nx, ny = x + direc[d][0], y + direc[d][1]
            chess_piece[n][2] = d
            if not in_range(nx, ny) or board[nx][ny] == blue: # 또 범위 밖 or 파란 칸
                continue

        pivot = locs[(x, y)].index(n) # 잘라낼 기준 (내 위 체스말만 데려가야 됨)
        if board[nx][ny] == white: # 하얀 칸
            company = locs[(x, y)][pivot:]
            locs[(x, y)] = locs[(x, y)][:pivot] # 떼내기
            locs[(nx, ny)].extend(company)
            if len(locs[(nx, ny)]) >= 4:
                return True
            for c in company:
                chess_piece[c][0], chess_piece[c][1] = nx, ny # 위치 갱신
        elif board[nx][ny] == red: # 빨간 칸
            company = locs[(x, y)][pivot:][::-1] # 빨간 칸은 역으로
            locs[(x, y)] = locs[(x, y)][:pivot]  # 떼내기
            locs[(nx, ny)].extend(company)
            if len(locs[(nx, ny)]) >= 4:
                return True
            for c in company:
                chess_piece[c][0], chess_piece[c][1] = nx, ny

    return False


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = [list(map(int, input().split())) for i in range(K)]
chess_piece = dict()
locs = defaultdict(list)
for i in range(K):
    x, y, d = order[i]
    locs[(x - 1, y - 1)].append(i)
    chess_piece[i] = [x - 1, y - 1, d - 1]

white, red, blue = 0, 1, 2
direc = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for i in range(1, 1000 + 1):
    if move():
        print(i)
        sys.exit()
print(-1)