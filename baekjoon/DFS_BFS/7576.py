from collections import deque


def isFinished():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return False
    return True


direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

q = deque()
first = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            first.append((i, j))

q.append([first, 0])
answer = 0
while q:
    points, day = q.popleft()
    if isFinished():
        answer = day
        break

    nexts = []
    for p in points:
        x, y = p
        for d in direction:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    nexts.append((nx, ny))
    if len(nexts) > 0:
        q.append([nexts, day + 1])

if not isFinished():
    print(-1)
else:
    print(answer)