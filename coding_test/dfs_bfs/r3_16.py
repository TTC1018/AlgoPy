from copy import deepcopy


def caculate_area():
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1
    return count


def spread_virus(x, y):
    for d in direction:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                spread_virus(nx, ny)


def dfs(count):
    global answer

    if count == 3:
        for i in range(N):
            temp[i] = deepcopy(area[i])

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    spread_virus(i, j)
        answer = max(answer, caculate_area())
        return

    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                area[i][j] = 1
                dfs(count + 1)
                area[i][j] = 0


N, M = map(int, input().split())
area = []
for _ in range(N):
    area.append(list(map(int, input().split())))
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
temp = [[0] * M for _ in range(N)]
answer = 0

dfs(0)
print(answer)
