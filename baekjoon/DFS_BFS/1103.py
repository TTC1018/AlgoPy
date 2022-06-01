import sys
sys.setrecursionlimit(10**9)
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def dfs(x, y, cnt):
    global answer, infinite
    if not graph[x][y]:
        answer = max(answer, cnt)
        return

    num = graph[x][y]
    for d in direc:
        nx, ny = x + num * d[0], y + num * d[1]
        if in_range(nx, ny):
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = False
            else:
                infinite = True
                return
        else:
            answer = max(answer, cnt + 1)
            continue

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(N):
    data = sys.stdin.readline().rstrip()
    if 'H' in data:
        data = data.replace('H', '0')
    graph.append(list(map(int, list(data))))

answer = 0
infinite = False
visited = [[False] * M for _ in range(N)]
visited[0][0] = True
dfs(0, 0, 0)

if infinite:
    print(-1)
else:
    print(answer)