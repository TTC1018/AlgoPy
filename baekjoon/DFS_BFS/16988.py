from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M
direc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def bfs():
    killed = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                immortal = False
                tmp_kill = 1
                while q:
                    qx, qy = q.popleft()
                    for d in direc:
                        nx, ny = qx + d[0], qy + d[1]
                        if in_range(nx, ny) and not visited[nx][ny]:
                            if not board[nx][ny]: # 0 하나라도 있으면 제거 불가
                                immortal = True # 연결된 나머지 2도 다 방문처리 되도록 break 하지는 않음
                            elif board[nx][ny] == 2:
                                visited[nx][ny] = True
                                tmp_kill += 1
                                q.append((nx, ny))

                if not immortal:
                    killed += tmp_kill
    return killed


def dfs(x, y, cnt):
    global answer
    if cnt == 2:
        answer = max(answer, bfs())
        return

    for j in range(y + 1, M): # 해당 행의 다음 열부터 탐색
        if not board[x][j]:
            board[x][j] = 1
            dfs(x, j, cnt + 1)
            board[x][j] = 0

    for i in range(x + 1, N): # 다음 행부터 탐색
        for j in range(M):
            if not board[i][j]:
                board[i][j] = 1
                dfs(i, j, cnt + 1)
                board[i][j] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            board[i][j] = 1
            dfs(i, j, 1)
            board[i][j] = 0
print(answer)