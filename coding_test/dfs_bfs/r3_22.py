from collections import deque

INF = int(1e9)

# 상, 하, 좌, 우
standard_move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 90도 회전
v_up_rot = [(1, 1), (1, -1)]
v_down_rot = [(-1, 1), (-1, -1)]
h_left_rot = [(1, 1), (-1, 1)]
h_right_rot = [(1, -1), (-1, -1)]


def solution(board):
    answer = INF

    b_len = len(board)
    visited = []
    q = deque([(0, (0, 0), (0, 1))])
    while q:
        count, first, second = q.popleft()
        fx, fy = first
        sx, sy = second

        if (fx == b_len - 1 and fy == b_len - 1) or (sx == b_len - 1 and sy == b_len - 1):
            answer = count
            break

        # 상하좌우
        for s_m in standard_move:
            nfx, nfy = fx + s_m[0], fy + s_m[1]
            nsx, nsy = sx + s_m[0], sy + s_m[1]
            if 0 <= nfx < b_len and 0 <= nfy < b_len and 0 <= nsx < b_len and 0 <= nsy < b_len:
                target_str = ''.join(list(map(str, [nfx, nfy, nsx, nsy])))
                if target_str not in visited and board[nfx][nfy] == 0 and board[nsx][nsy] == 0:
                    visited.append(target_str)
                    q.append((count + 1, (nfx, nfy), (nsx, nsy)))
        # 90도 회전
        if fx == sx:  # 수평일 때
            for idx, h_lr in enumerate(h_left_rot):
                nfx, nfy = fx + h_lr[0], fy + h_lr[1]
                if 0 <= nfx < b_len and 0 <= nfy < b_len:
                    target_str = ''.join(list(map(str, [nfx, nfy, sx, sy])))
                    if target_str not in visited and board[nfx][nfy] != 1:
                        if idx == 0 and board[fx + 1][fy] != 1:
                            target_str = ''.join(list(map(str, [sx, sy, nfx, nfy])))
                            q.append((count + 1, (sx, sy), (nfx, nfy)))
                        elif idx == 1 and board[fx - 1][fy] != 1:
                            q.append((count + 1, (nfx, nfy), (sx, sy)))
                        visited.append(target_str)
            for idx, h_rr in enumerate(h_right_rot):
                nsx, nsy = sx + h_rr[0], sy + h_rr[1]
                if 0 <= nsx < b_len and 0 <= nsy < b_len:
                    target_str = ''.join(list(map(str, [fx, fy, nsx, nsy])))
                    if target_str not in visited and board[nsx][nsy] != 1:
                        if idx == 0 and board[sx + 1][sy] != 1:
                            q.append((count + 1, (fx, fy), (nsx, nsy)))
                        elif idx == 1 and board[sx - 1][sy] != 1:
                            target_str = ''.join(list(map(str, [nsx, nsy, fx, fy])))
                            q.append((count + 1, (nsx, nsy), (fx, fy)))
                        visited.append(target_str)
        elif fy == sy:  # 수직일 때
            for idx, v_ur in enumerate(v_up_rot):
                nfx, nfy = fx + v_ur[0], fy + v_ur[1]
                if 0 <= nfx < b_len and 0 <= nfy < b_len:
                    target_str = ''.join(list(map(str, [nfx, nfy, sx, sy])))
                    if target_str not in visited and board[nfx][nfy] != 1:
                        if idx == 0 and board[fx][fy + 1] != 1:
                            target_str = ''.join(list(map(str, [sx, sy, nfx, nfy])))
                            q.append((count + 1, (sx, sy), (nfx, nfy)))
                        elif idx == 1 and board[fx][fy - 1]:
                            q.append((count + 1, (nfx, nfy), (sx, sy)))
                        visited.append(target_str)
            for idx, v_dr in enumerate(v_down_rot):
                nsx, nsy = sx + v_dr[0], sy + v_dr[1]
                if 0 <= nsx < b_len and 0 <= nsy < b_len:
                    target_str = ''.join(list(map(str, [fx, fy, nsx, nsy])))
                    if target_str not in visited and board[nsx][nsy] != 1:
                        if idx == 0 and board[sx][sy + 1] != 1:
                            q.append((count + 1, (fx, fy), (nsx, nsy)))
                        elif idx == 1 and board[sx][sy - 1] != 1:
                            target_str = ''.join(list(map(str, [nsx, nsy, fx, fy])))
                            q.append((count + 1, (nsx, nsy), (fx, fy)))
                        visited.append(target_str)
    return answer


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
