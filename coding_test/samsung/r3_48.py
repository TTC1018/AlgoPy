def time_flow():
    for i in range(N):
        for j in range(N):
            if smell_graph[i][j][1] > 0:
                smell_graph[i][j][1] -= 1 # 1초 감소
            if graph[i][j] != 0:
                smell_graph[i][j] = [graph[i][j], k]


def isFinished():
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                count += 1
    
    if count > 1: # 상어가 2마리 이상 남아있을 때
        return False    
    return True

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def shark_move():
    for s in range(1, M + 1): # 상어 M마리 순차적으로 움직이기
        for i in range(N):
            for j in range(N):
                if graph[i][j] == s:
                    void_flag = False
                    for n_d in s_prior[s - 1][s_direc[s - 1]]:
                        n_d -= 1
                        nx, ny = i + d[n_d][0], j + d[n_d][1]
                        if 0 <= nx < N and 0 <= ny < N: # 범위 내 일때
                            if smell_graph[nx][ny][1] == 0: # 빈 공간 일때
                                graph[i][j] = 0 # 지난 자리 비우기
                                s_locs[s - 1] = [nx, ny] # 현재 위치 변경
                                s_direc[s - 1] = n_d # 방향 변경
                                void_flag = True
                                break
                    
                    if not void_flag: # 빈 공간으로 이동 안 했을 때
                        for n_d in s_prior[s - 1][s_direc[s - 1]]:
                            n_d -= 1
                            nx, ny = i + d[n_d][0], j + d[n_d][1]
                            if 0 <= nx < N and 0 <= ny < N:
                                if smell_graph[nx][ny][0] == s: # 자기 냄새 있는 공간일 때
                                    graph[i][j] = 0 # 지난 자리 비우기
                                    s_locs[s - 1] = [nx, ny] # 현재 위치 변경
                                    s_direc[s - 1] = n_d # 방향 변경
                                    break


def overlap_check():
    for idx in range(M):
        if s_locs[idx] != [None, None]:
            for idx2 in range(idx + 1, M):
                if s_locs[idx] == s_locs[idx2]: # 겹치는 상어 있을 때
                    x, y = s_locs[idx]
                    graph[x][y] = idx + 1 # 작은 인덱스 상어가 자리 차지
                    s_locs[idx2] = [None, None]
    
    for idx, s_loc in enumerate(s_locs): # 겹치지 않는 곳도 위치 갱신
        if s_loc != [None, None]:
            x, y = s_loc
            graph[x][y] = idx + 1
                    
                        
N, M, k = map(int, input().split())

s_locs = [[0, 0] for _ in range(M)]
graph = []
smell_graph = [[[0, 0]] * N for _ in range(N)]
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] != 0:
            s_locs[data[j] - 1] = [i, j]
    graph.append(data)

s_direc = list(map(int, input().split()))
for i in range(M):
    s_direc[i] -= 1
s_prior = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
# 1. 냄새없는 칸으로
# 2. 그런 칸이 없다면 자신의 냄새가 있는 칸으로
# 3. 가능한 칸이 여러 개라면 우선순위에 따라서
# 한 칸에 여러 마리 상어가 남으면, 가장 작은 번호 상어만 남기고 상어 제거
# 1번 상어만 남을 때까지 진행, 1000초가 지나도 불가능하면 -1 리턴
second = 0
while True:
    second += 1
    time_flow() # 냄새 시간 흐르기
    shark_move() # 상어 움직이기
    overlap_check()# 겹치는 상어 계산 및 빈칸을 냄새칸으로 처리    
    if isFinished() or second > 1000:
        break

if second > 1000:
    second = -1
print(second)