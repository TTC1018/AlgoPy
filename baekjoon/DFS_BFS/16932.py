from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M

direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
area = [[0] * M for _ in range(N)]

area_val = [-1] # 특정 지역번호에 몇개의 칸이 소속되나 기록
area_num = 1
visited = [[False] * M for _ in range(N)]
# 각 좌표에 모양 이루는 지역 기록하기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            area[i][j] = area_num
            area_cnt = 1
            while q:
                x, y = q.popleft()
                for d in direc:
                    nx, ny = x + d[0], y + d[1]
                    if in_range(nx, ny) and graph[nx][ny]:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            area[nx][ny] = area_num
                            area_cnt += 1
            area_val.append(area_cnt)
            area_num += 1

# 기록한 지역번호를 활용하며 상하좌우 확인 후 계산
answer = 0
for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            g_cnt = 1
            visited = set() # area_num의 최대값이 클 수도 있으므로 배열 생성대신 set을 활용
            for d in direc:
                ni, nj = i + d[0], j + d[1]
                if in_range(ni, nj) and area[ni][nj]:
                    area_number = area[ni][nj]
                    if area_number not in visited:
                        visited.add(area_number)
                        g_cnt += area_val[area_number]
            answer = max(answer, g_cnt)
print(answer)