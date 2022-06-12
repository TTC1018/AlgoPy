import sys
sys.setrecursionlimit(10**5)
in_range = lambda x, y: 0 <= x < N and 0 <= y < M
INF = int(1e9)

def dfs(x, y, prev_d):
    if x == N - 1 and y == M - 1:
        return graph[x][y]

    if dp[x][y][prev_d] == -INF:
        for i in range(3):
            nx, ny = x + direc[i][0], y + direc[i][1]
            if (prev_d == 1 and i == 2) or (prev_d == 2 and i == 1): # 간 곳 또가는 경우
                continue

            if in_range(nx, ny):
                dp[x][y][prev_d] = max(dp[x][y][prev_d], dfs(nx, ny, i) + graph[x][y])
    return dp[x][y][prev_d]


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direc = [(1, 0), (0, 1), (0, -1)]
dp = [[[-INF] * 3 for _ in range(M)] for _ in range(N)]
print(dfs(0, 0, 0)) # 0, 0은 시작점이라 이전 방향 없으므로 1, 2를 대신할 인덱스를 넣어줌 (if문 조건에 걸리지 않도록)

for p in dp:
    print(*p)