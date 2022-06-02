import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def dfs(x, y, cnt):
    global answer
    if not graph[x][y]:
        answer = max(answer, cnt)
        return

    num = graph[x][y]
    for d in direc:
        nx, ny = x + num * d[0], y + num * d[1]
        if in_range(nx, ny) and dp[nx][ny] < cnt + 1:
            if not visited[nx][ny]:
                dp[nx][ny] = cnt + 1
                visited[nx][ny] = True
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = False
            else:
                print(-1)
                sys.exit()
        else: # 범위 벗어났을 때
            answer = max(answer, cnt + 1)
            continue


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(N): # H는 숫자 0으로 변환
    data = sys.stdin.readline().rstrip()
    if 'H' in data:
        data = data.replace('H', '0')
    graph.append(list(map(int, list(data))))

answer = 0
visited = [[False] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
visited[0][0] = True
dfs(0, 0, 0)
print(answer)