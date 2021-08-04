def solve(x, y, depth):
    if visited[x][y][depth] >= 0:
        return visited[x][y][depth]

    if alphas[x][y] != target[depth]:
        visited[x][y][depth] = 0
        return 0

    depth += 1
    if depth == len(target):
        visited[x][y][depth - 1] = 1
        return 1

    count = 0
    for i in range(-K, K + 1):
        if i == 0:
            continue

        new_x, new_y = x + i, y + i
        if 0 <= new_x < N:
            count += solve(new_x, y, depth)
        if 0 <= new_y < M:
            count += solve(x, new_y, depth)
    visited[x][y][depth - 1] = count
    return count


N, M, K = [int(n) for n in input().split(' ')]
alphas = []
for i in range(N):
    alphas.append(list(input()))
target = input()
visited = [[[-1] * len(target) for j in range(M)] for i in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if alphas[i][j] == target[0]:
            answer += solve(i, j, 0)
print(answer)