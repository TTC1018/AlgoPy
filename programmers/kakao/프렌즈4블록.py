from collections import defaultdict
in_range = lambda x, y: 0 <= x < R and 0 <= y < C


def drop(board):
    for j in range(C):
        for i in range(R - 2, -1, -1):
            idx = i
            while idx < R - 1 and board[idx + 1][j] == 'X':
                idx += 1
            board[idx][j], board[i][j] = board[i][j], board[idx][j]
    return board


direc = [(0, 1), (1, 0), (1, 1)]
def explode(board):
    alpha_dict = defaultdict(set)

    result = 0
    e_flag = False
    for i in range(R):
        for j in range(C):
            name = board[i][j]
            if name != 'X':
                locs = set()
                locs.add((i, j))
                for d in direc:
                    ni, nj = i + d[0], j + d[1]
                    if in_range(ni, nj) and board[ni][nj] == name:
                        locs.add((ni, nj))
                    else:
                        break
                else:
                    if len(locs) == 4:
                        alpha_dict[name].update(locs)
                        e_flag = True

    # print(alpha_dict)
    for name in alpha_dict:
        result += len(alpha_dict[name])
        for x, y in alpha_dict[name]:
            board[x][y] = 'X'

    board = drop(board)
    # for b in board:
    #     print(*b)

    if e_flag:
        result += explode(board)

    return result



R, C = 0, 0
def solution(m, n, board):
    global R, C
    R, C = m, n
    board = [list(b) for b in board]
    return explode(board)

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	))