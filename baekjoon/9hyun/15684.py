import sys
input = sys.stdin.readline
INF = int(1e9)
# 위치 좌표는 가로선 세로선 교차점이므로
# H * N 개 존재
def laddering():
    for i in range(N):
        y = i
        for x in range(H):
            if y < N - 1 and widths[x][y]:
                y += 1
            elif y > 0 and widths[x][y - 1]:
                y -= 1
        if y != i:
            return False
    return True


def dfs(idx, count, limit):
    global answer

    if count == limit:
        if laddering():
            answer = count
        return

    for i in range(idx, H):
        for j in range(N - 1):
            if not widths[i][j]:
                widths[i][j] = True
                dfs(i, count + 1, limit)
                widths[i][j] = False


N, M, H = map(int, input().split())
# N = 열 개수, H = 행 개수
# 두 가로선이 연속되면 안 됨
# i번의 결과가 i번에 나오도록 하기
widths = [[False] * (N - 1) for _ in range(H)] # 가로선
answer = INF
for _ in range(M):
    x, y = map(int, input().split())
    widths[x - 1][y - 1] = True

for i in range(4):
    dfs(0, 0, i)
    if answer != INF:
        break

if answer == INF:
    print(-1)
else:
    print(answer)