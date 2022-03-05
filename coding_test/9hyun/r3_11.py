N = int(input())
K = int(input())
apple = [[False] * N for _ in range(N)]
for _ in range(N):
    R, C = map(int, input().split())
    apple[R - 1][C - 1] = True
L = int(input())

graph = [[False] * N for _ in range(N)]
graph[0][0] = True
# 벽 or 자기 몸에 부딪히면 게임 종료
for _ in range(L):
    X, C = input().split()
    X = int(X)


