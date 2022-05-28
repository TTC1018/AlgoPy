import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


def dfs(x, y):
    global answer
    if not in_range(x, y):
        return True

    if maze[x][y] == 'Y':
        return True
    elif maze[x][y] == 'N':
        return False

    ret = False
    if not visited[x][y]:
        visited[x][y] = True
        nx, ny = x + direc[maze[x][y]][0], y + direc[maze[x][y]][1]
        if dfs(nx, ny):
            maze[x][y] = 'Y'
            ret = True
        else:
            maze[x][y] = 'N'
            ret = False
    return ret


direc = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            answer += 1
print(answer)