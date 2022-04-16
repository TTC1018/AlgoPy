import sys
input = sys.stdin.readline


def four_seasons():

    # 봄
    for i in range(N):
        for j in range(N):
            t_len = len(tree[i][j])
            for k in range(t_len):
                if tree[i][j][k] <= graph[i][j]:
                    graph[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    # 여름
                    for _ in range(t_len - k):
                        graph[i][j] += tree[i][j].pop() // 2
                    break


    # 가을
    for i in range(N):
        for j in range(N):
            for age in tree[i][j]:
                if age % 5 == 0:
                    for d in direc:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < N and 0 <= nj < N:
                            tree[ni][nj].insert(0, 1)

    # 겨울
    for i in range(N):
        for j in range(N):
            graph[i][j] += A[i][j]


direc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
graph = [[5] * N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())  # 위치 및 나이
    tree[x - 1][y - 1].append(z)

# 메인코드
for _ in range(K):
    four_seasons()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])
print(answer)
