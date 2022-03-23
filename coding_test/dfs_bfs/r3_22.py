INF = int(1e9)

#상, 하, 좌, 우
standard_move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#90도 회전
v_up_rot = [(1, 1), (1, -1)]
v_down_rot = [(-1, 1), (-1, -1)]
h_left_rot = [(1, 1), (-1, 1)]
h_right_rot = [(1, -1), (-1, -1)]

def dfs(first, second, count):
    global answer
    
    fx, fy = first
    sx, sy = second
    
    if (fx == b_len -1 and fy == b_len - 1) or (sx == b_len - 1 and sy == b_len -1):
        answer = min(answer, count)
        return
    
    # 상하좌우
    for s_m in standard_move:
        nfx, nfy = fx + s_m[0], fy + s_m[1]
        nsx, nsy = sx + s_m[0], sy + s_m[1]
        if 0 <= nfx < b_len and 0 <= nfy < b_len and 0 <= nsx < b_len and 0 <= nsy < b_len:
            if not (visited[nfx][nfy] and visited[nsx][nsy]):
                visited[nfx][nfy] = True
                visited[nsx][nsy] = True
                dfs((nfx, nfy), (nsx, nsy), count + 1)
                visited[nfx][nfy] = False
                visited[nsx][nsy] = False
    # 90도 회전
    if fx == sx: # 수평일 때
        for idx, h_lr in enumerate(h_left_rot):
            nfx, nfy = fx + h_lr[0], fy + h_lr[1]
            if 0 <= nfx < b_len and 0 <= nfy < b_len:
                if not (visited[nfx][nfy] and visited[sx][sy]):
                    visited[nfx][nfy] = True
                    if idx == 0:
                        dfs((sx, sy), (nfx, nfy), count + 1)
                    else:
                        dfs((nfx, nfy), (sx, sy), count + 1)
                    visited[nfx][nfy] = False
        for idx, h_rr in enumerate(h_right_rot):
            nsx, nsy = sx + h_rr[0], sy + h_rr[1]
            if 0 <= nsx < b_len and 0 <= nsy < b_len:
                if not (visited[fx][fy] and visited[nsx][nsy]):
                    visited[nsx][nsy] = True
                    if idx == 0:
                        dfs((fx, fy), (nsx, nsy), count + 1)
                    else:
                        dfs((nsx, nsy), (fx, fy), count + 1)
                    visited[nsx][nsy] = False
    else: # 수직일 때
        for idx, v_ur in enumerate(v_up_rot):
            nfx, nfy = fx + v_ur[0], fy + v_ur[1]
            if 0 <= nfx < b_len and 0 <= nfy < b_len:
                if not (visited[nfx][nfy] and visited[sx][sy]):
                    visited[nfx][nfy] = True
                    if idx == 0:
                        dfs((sx, sy), (nfx, nfy), count + 1)
                    else:
                        dfs((nfx, nfy), (sx, sy), count + 1)
                    visited[nfx][nfy] = False
        for idx, v_dr in enumerate(v_down_rot):
            nsx, nsy = sx + v_dr[0], sy + v_dr[1]
            if 0 <= nsx < b_len and 0 <= nsy < b_len:
                if not (visited[fx][fy] and visited[nsx][nsy]):
                    visited[nsx][nsy] = True
                    if idx == 0:
                        dfs((fx, fy), (nsx, nsy), count + 1)
                    else:
                        dfs((nsx, nsy), (fx, fy), count + 1)
                    visited[nsx][nsy] = False
    

b_len = 0
visited = []
answer = INF
def solution(board):
    global answer
    
    b_len = len(board)
    visited = [[False] * b_len for _ in range(b_len)]
    visited[0][0], visited[0][1] = True, True
    dfs((0, 0), (0, 1), 0)
    return answer

print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))