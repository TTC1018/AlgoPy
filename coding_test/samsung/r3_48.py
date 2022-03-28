def time_flow():
    for i in range(N):
        for j in range(N):
            if time_graph[i][j] > 0:
                time_graph[i][j] -= 1
                if time_graph[i][j] == 0:
                    graph[i][j] = 0


def isFinished():
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                count += 1
    
    if count > 1:
        return False    
    return True

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def shark_move():
    for s in range(M): # 상어 M마리 순차적으로 움직이기
        for i in range(N):
            for j in range(N):
                if graph[i][j] == s:
                    void_flag = False
                    for next in range(s_direc[s], s_direc[s] + 4):
                        nx, ny = i + d[next % 4]
                        if 0 <= nx < N and 0 <= ny < N: # 범위 내 일때
                            if graph[nx][ny] == 0: # 빈 공간 일 때
                                time_graph[nx][ny] = k # 냄새 적용
                                s_direc[s] = next % 4
                                void_flag = True
                                break
                    
                    if not void_flag: # 빈 공간으로 이동 안 했을 때
                        
                        
                    
                        
                    
                        
N, M, k = map(int, input().split())

s_locs = [(0, 0)] * M
graph = []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] != 0:
            s_locs[data[j]] = (i, j)
    graph.append(data)


time_graph = [[0] * N for _ in range(N)]


s_direc = list(map(int, input().split()))
for i in range(M):
    s_direc[i] -= 1

s_prior = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

# 1. 냄새없는 칸으로
# 2. 그런 칸이 없다면 자신의 냄새가 있는 칸으로
# 3. 가능한 칸이 여러 개라면 우선순위에 따라서
# 한 칸에 여러 마리 상어가 남으면, 가장 작은 번호 상어만 남기고 상어 제거
# 1번 상어만 남을 때까지 진행, 1000초가 지나도 불가능하면 -1 리턴
while True:
    time_flow() # 냄새 시간 흐르기
    shark_move() # 상어 움직이기
    # 겹치는 상어 계산 및 빈칸을 냄새칸으로 처리
    
    if isFinished():
        break