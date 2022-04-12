INF = int(1e9)
# 위치 좌표는 가로선 세로선 교차점이므로
# M * N 개 존재
# 가능한 진행 경로 = 아래(-1, 0) OR 오른쪽 (0, 1) OR 왼쪽 (0, -1)
direc = [(0, 1), (0, -1), (-1, 0)]
def laddering():
    for i in range(M):
        x, y = 0, i
        for d in direc:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < M and 0 <= ny < N:
                pass


def dfs(col, pos, count):
    global answer

    x, y = pos
    if y == M - 1:
        if x == col:
            answer = min(answer, count)
        return
    if count == H:
        return




N, M, H = map(int, input().split())
# N - 1 = 열 개수, M = 행 개수
# 두 가로선이 연속되면 안 됨
# i번의 결과가 i번에 나오도록 하기

widths = [[False] * (N - 1) for _ in range(M)] # 가로선
answer = INF
