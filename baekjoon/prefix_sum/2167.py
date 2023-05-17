import sys
input = sys.stdin.readline


N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
P = [[0] * M for _ in range(N)]
P[0][0] = B[0][0]
for i in range(1, M):
    P[0][i] += B[0][i] + P[0][i - 1]
for i in range(1, N):
    P[i][0] += B[i][0] + P[i - 1][0]
for i in range(1, N):
    for j in range(1, M):
        P[i][j] = B[i][j] + (P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1])

K = int(input())
for _ in range(K):
    i, j, x, y = map(lambda x: int(x) - 1, input().split())
    if i == 0 and j == 0:
        print(P[x][y])
    elif i == 0:
        print(P[x][y] - P[x][j - 1])
    elif j == 0:
        print(P[x][y] - P[i - 1][y])
    else:
        print(P[x][y] - P[i - 1][y] - P[x][j - 1] + P[i - 1][j - 1])
