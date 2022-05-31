import sys
in_range = lambda x, y: 0 <= x < R and 0 <= y < C


def dfs(x, y):
    global answer
    if y == C - 1:
        answer += 1
        return True

    for d in direc:
        nx, ny = x + d[0], y + d[1]
        if in_range(nx, ny) and graph[nx][ny] == '.':
            if not visited[nx][ny]:
                visited[nx][ny] = True # 앞서 탐색한 실패 루트를 마주치면 종료되야 하므로, 다시 False로 바꾸지 않음
                if dfs(nx, ny):
                    return True
    return False



direc = [(-1, 1), (0, 1), (1, 1)]
R, C = map(int, sys.stdin.readline().rstrip().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
answer = 0
for row in range(R):
    dfs(row, 0)
print(answer)