from collections import deque

N, K = map(int, input().split())
q = deque() # BFS 풀이

graph = []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] != 0:
            q.append((data[j], i, j)) # 바이러스가 있는 위치를 기록
    graph.append(data)

S, X, Y = map(int, input().split())
q = deque(sorted(q, key=lambda x:x[0])) # 숫자가 낮은 바이러스부터 시작해야 되므로 정렬

direc = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
second, t_sec = 0, len(q) # 1초가 지났는 지를 확인 하려면 현재 큐의 길이를 초를 세는 단위로 이용하면 된다
while q:
    if second == S:
        break

    virus, x, y = q.popleft()
    for d in direc:
        nx, ny = x + d[0], y + d[1] # 새로운 위치
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0: # 바이러스를 퍼뜨릴 수 있는 위치
                graph[nx][ny] = virus # 바이러스 퍼뜨리기
                q.append((virus, nx, ny)) # 큐에 등록
    t_sec -= 1

    if t_sec == 0: # 해당 분기가 끝났을 때가 1초가 지난 것
        second += 1
        t_sec = len(q) # 새로운 분기가 시작됐음을 기록

print(graph[X - 1][Y - 1])