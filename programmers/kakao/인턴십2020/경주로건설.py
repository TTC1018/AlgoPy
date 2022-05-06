from collections import deque


INF = int(1e9)
direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs(board, x, y, prev_d, cost): 
    b_len = len(board)
    visited = [[INF] * b_len for _ in range(b_len)]
    visited[0][0] = 0
    visited[x][y] = 100
    
    q = deque()
    q.append([x, y, prev_d, cost])
    result = INF
    while q:
        qx, qy, p_d, cst = q.popleft()
        if (qx, qy) == (b_len - 1, b_len - 1):
            result = min(result, cst)
            continue

        for d_idx, d in enumerate(direc):
            nx, ny = qx + d[0], qy + d[1]
            if 0 <= nx < b_len and 0 <= ny < b_len:
                if board[nx][ny] == 0:
                    if d_idx == p_d:
                        if cst + 100 < visited[nx][ny]:
                            visited[nx][ny] = cst + 100
                            q.append([nx, ny, d_idx, cst + 100])
                    else:
                        if cst + 600 < visited[nx][ny]:
                            visited[nx][ny] = cst + 600
                            q.append([nx, ny, d_idx, cst + 600])
    return result


def solution(board):
    # 맨처음 가능한 경우 = 우측, 아래
    answer = INF
    if board[1][0] == 0:
        answer = min(answer, bfs(board, 1, 0, 1, 100))
    if board[0][1] == 0:
        answer = min(answer, bfs(board, 0, 1, 2, 100))
    
    return answer
print(solution([[0,0,0],[0,0,0],[0,0,0]]))