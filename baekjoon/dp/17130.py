import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M
d = [(1, -1), (-1, -1), (0, -1)]

N, M = map(int, input().split())
G = []
dp = [[-1] * M for _ in range(N)]
rx, ry = 0, 0
for i in range(N):
    row = input().rstrip()
    for j in range(M):
        if row[j] == 'R':
            rx, ry = i, j
    G.append(row)
dp[rx][ry] = 0

answer = -1
for j in range(1, M):
    for i in range(N):
        if G[i][j] != '#':
            for dx, dy in d:
                px, py = i + dx, j + dy
                if in_range(px, py) and G[px][py] != '#':
                    dp[i][j] = max(dp[i][j], dp[px][py])

            if dp[i][j] != -1:
                if G[i][j] == 'C':
                    dp[i][j] += 1
                elif G[i][j] == 'O':
                    answer = max(answer, dp[i][j])

print(answer)
