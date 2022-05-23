import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


def dfs(x, y, d):
    global answer

    if x == N - 1 and y == N - 1:
        answer += 1
        return

    for d_idx in range(3):
        nx, ny = x + direc[d_idx][0], y + direc[d_idx][1]
        if in_range(nx, ny) and not graph[nx][ny]:
            if d_idx == 1:
                if not graph[nx - 1][ny] and not graph[nx][ny - 1]:
                    dfs(nx, ny, d_idx)
            else:
                if d in [d_idx, 1]:
                    dfs(nx, ny, d_idx)


direc = [(0, 1), (1, 1), (1, 0)]
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
if graph[N - 1][N - 1]:
    print(0)
    sys.exit()

answer = 0
dfs(0, 1, 0)
print(answer)