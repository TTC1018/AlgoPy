import sys
sys.setrecursionlimit(25000) 
# 시간 내에 풀리는 코드인데, recursion 제한 때문에 채점이 멈추므로 제한을 풀어줌


def isEmpty(list_val): # 인구 이동 대상이 있는지 확인하는 코드
    for lists in list_val:
        for l in lists:
            if len(l) > 1: # 자기 자신 이외에 다른 좌표가 있는지 확인
                return False
    return True

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(start, origin):
    x, y = start
    
    for d in direction:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and L <= abs(A[x][y] - A[nx][ny]) <= R:
                visited[nx][ny] = True
                divs[origin[0]][origin[1]].append((nx, ny))
                dfs((nx, ny), origin)


N, L, R = map(int, input().split())
visited = [[False] * N for _ in range(N)]
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

divs = [[[(i, j)] for j in range(N)] for i in range(N)] # dfs 출발 지점과 연결된 연합을 나타내는 리스트
day = 0
while True:
    # 모든 좌표에 dfs로 확인
    for i in range(N):
        for j in range(N):
            visited[i][j] = True
            dfs((i, j), (i, j))
            
    # 인구 이동대상이 있는지 확인
    if isEmpty(divs): # 없을 때
        break
    else:
        day += 1
        # 인구 이동
        for div in divs:
            for d in [d for d in div if len(d) > 1]: # 인구 이동대상이 있는 연합만 계산
                sum_val, cnt_val = 0, len(d)
                #연합의 인구수
                for dx, dy in d:
                    sum_val += A[dx][dy]
                #계산
                for dx, dy in d:
                    A[dx][dy] = (sum_val // cnt_val)
                
        # 초기화 (visited 리스트와 연합 리스트)
        for i in range(N):
            for j in range(N):
                visited[i][j] = False
        divs = [[[(i, j)] for j in range(N)] for i in range(N)]
print(day)