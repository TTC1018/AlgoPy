import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < 5 and 0 <= y < 5


def dfs(case, s_cnt, y_cnt):
    global answer
    if y_cnt >= 4:
        return
    if s_cnt + y_cnt == 7:
        bit = 0
        for c in case:
            bit |= 1 << c
        if bit not in visited:
            visited.add(bit)
            answer += 1
        return
    for pos in case:
        x, y = divmod(pos, 5)
        for d in direc:
            nx, ny = x + d[0], y + d[1]
            nxt = nx * 5 + ny
            if in_range(nx, ny) and nxt not in case:
                if graph[nx][ny] == 'Y':
                    dfs(case + [nxt], s_cnt, y_cnt + 1)
                else:
                    dfs(case + [nxt], s_cnt + 1, y_cnt)


direc = [(-1, 0), (0, 1), (0, -1), (1, 0)]
graph = [list(input()) for _ in range(5)]
visited = set()
answer = 0
for i in range(5):
    for j in range(5):
        if graph[i][j] == 'S':
            dfs([i*5 + j], 1, 0)
print(answer)