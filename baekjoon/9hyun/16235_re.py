import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N
t_direc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def four_seasons():
    for x in range(N):
        for y in range(N):
            t_len = len(tree[x][y])
            for i in range(t_len):
                if tree[x][y][i] > field[x][y]:  # 먹을 양분 없을 때
                    # 여름 처리
                    for _ in range(i, t_len):
                        field[x][y] += (tree[x][y].pop() // 2)
                    break  # 어차피 뒤에 나무도 못 먹음

                field[x][y] -= tree[x][y][i]
                tree[x][y][i] += 1

    for x in range(N):
        for y in range(N):
            for i in range(len(tree[x][y])):
                if not tree[x][y][i] % 5:
                    for d in t_direc:
                        nx, ny = x + d[0], y + d[1]
                        if in_range(nx, ny):
                            tree[nx][ny].insert(0, 1)


    for i in range(N):
        for j in range(N):
            field[i][j] += A[i][j]


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
field = [[5] * N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    tree[x][y].append(z)

for i in range(N):
    for j in range(N):
        if tree[i][j]:
            tree[i][j].sort()

for _ in range(K):
    four_seasons()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])
print(answer)