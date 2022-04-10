from collections import deque

direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
s_flag = False
def is_seperated():
    global s_flag

    result = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] != 0:
                result += 1
                visited[i][j] = True
                q = deque([(i, j)])
                while q:
                    now = q.popleft()
                    x, y = now
                    for d in direc:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < N and 0 <= ny < M:
                            if graph[nx][ny] != 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    if result > 1:
        s_flag = True
        return True
    return False


def no_ice():
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                return False
    return True


def time_flow():
    targets = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                count = 0
                for d in direc:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < N and 0 <= nj < M:
                        if graph[ni][nj] == 0:
                            count += 1
                targets.append(((i, j), count))
    for t, cnt in targets:
        graph[t[0]][t[1]] = max(graph[t[0]][t[1]] - cnt, 0)


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# 바다 0
# 1년마다 동서남북 0개수만큼 높이가 줄어듦
# 두 덩어리 이상으로 분리되는 최초의 시간은?

answer = 0
while True:
    answer += 1
    time_flow()
    if is_seperated() or no_ice():
        break

if not s_flag:
    print(0)
else:
    print(answer)