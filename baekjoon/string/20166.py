import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


def dfs(x, y, idx, limit, target):
    global cnt
    if idx == limit:
        cnt += 1
        return

    for i in range(8):
        nx, ny = x + direc[i][0], y + direc[i][1]
        if in_range(nx, ny):
            if graph[nx][ny] == target[idx]:
                dfs(nx, ny, idx + 1, limit, target)
        else:
            if i < 4:
                if nx < 0 or nx >= N:
                    nx = 0 if nx == N else N - 1
                elif ny < 0 or ny >= M:
                    ny = 0 if ny == M else M - 1
            else:
                if nx < 0 or nx >= N:
                    nx = 0 if nx == N else N - 1
                if ny < 0 or ny >= M:
                    ny = 0 if ny == M else M - 1

            if graph[nx][ny] == target[idx]:
                dfs(nx, ny, idx + 1, limit, target)


direc = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
N, M, K = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]
favorite = [input().rstrip() for _ in range(K)]

cnt_dict = {}
for f in favorite:
    if f not in cnt_dict:
        cnt = 0

        for i in range(N):
            for j in range(M):
                if f[0] == graph[i][j]:
                    dfs(i, j, 1, len(f), f)
        cnt_dict[f] = cnt
        print(cnt)
    else:
        print(cnt_dict[f])