from collections import deque
INF = int(1e9)
direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

q = deque()
q.append(((0, 0), 1))

answer = INF
while q:
    point, count = q.popleft()
    x, y = point
    
    if x == N - 1 and y == M - 1:
        answer = min(answer, count)
        break
    
    
    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append(((nx, ny), count + 1))
print(answer)