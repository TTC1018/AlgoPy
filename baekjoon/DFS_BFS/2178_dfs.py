import sys
input = sys.stdin.readline


INF = int(1e9)
direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(start, count):
    global answer
    
    x, y = start
    if count >= answer:
        return
    if x == N - 1 and y == M - 1:
        answer = min(answer, count)
        return
    
    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs((nx, ny), count + 1)
                visited[nx][ny] = False
    


N, M = map(int, input().split())
maze = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
visited[0][0] = True

answer = INF
dfs((0, 0), 1)
print(answer)