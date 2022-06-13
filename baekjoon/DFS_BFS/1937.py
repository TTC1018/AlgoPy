import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < n and 0 <= y < n

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 1

        max_val = 0
        for d in direc:
            nx, ny = x + d[0], y + d[1]
            if in_range(nx, ny) and bamboo[x][y] < bamboo[nx][ny]:
                max_val = max(max_val, dfs(nx, ny))
        dp[x][y] += max_val
    return dp[x][y]


direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)