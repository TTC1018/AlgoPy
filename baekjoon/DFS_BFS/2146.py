from collections import deque
INF = int(1e9)

direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 0 = 바다, 1 = 육지
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
i_num = [[0] * N for _ in range(N)]

# 섬 번호 매기기
temp_num = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and i_num[i][j] == 0:
            q = deque()
            q.append((i, j))
            i_num[i][j] =  temp_num
            while q:
                x, y = q.popleft()
                for d in direc:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] == 1 and i_num[nx][ny] == 0:
                            i_num[nx][ny] = temp_num
                            q.append((nx, ny))
            temp_num += 1

# 다리 놓기
answer = INF
for area in range(1, temp_num):
    q = deque()
    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and i_num[i][j] == area:
                q.append((i, j))
                dist[i][j] = 1
    
    a_temp = INF
    while q:
        x, y = q.popleft()
        for d in direc:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and i_num[nx][ny] != area:
                    a_temp = dist[x][y] - 1 # 처음에 값 1로 시작했으므로 1 빼줌
                    q.clear()
                    break
                if graph[nx][ny] == 0 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    answer = min(answer, a_temp)

print(answer)