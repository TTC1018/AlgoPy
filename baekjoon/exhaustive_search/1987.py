def solve(x, y):
    global answer
    q = {(x, y, alphas[x][y])}

    while q:
        x, y, temp_a = q.pop()

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < R and 0 <= new_y < C and alphas[new_x][new_y] not in temp_a:
                q.add((new_x, new_y, temp_a + alphas[new_x][new_y]))
                answer = max(answer, len(temp_a) + 1)


R, C = [int(n) for n in input().split(' ')]
alphas = []
for i in range(R):
    alphas.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 1
passed = set(alphas[0][0])
solve(0, 0)
print(answer)