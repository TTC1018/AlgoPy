def dfs(start):
    global answer
    visited[start] = 1
    for idx, next in enumerate(m[start]):
        if next == 1 and visited[idx] == -1:
            answer += 1
            dfs(idx)


N = int(input())
M = int(input())

m = [[0] * N for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    m[x - 1][y - 1] = 1
    m[y - 1][x - 1] = 1
visited = [-1] * N

answer = 0
dfs(0)
print(answer)