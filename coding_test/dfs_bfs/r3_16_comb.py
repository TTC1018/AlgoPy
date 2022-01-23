import sys
from itertools import combinations
input = sys.stdin.readline


def area_sum():
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1
    return count


def spread_v(x, y):
    for d in direction:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                spread_v(nx, ny)


N, M = map(int, input().split())
cands = []
m = []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if data[j] == 0:
            cands.append((i, j)) # 벽을 세울 수 있는 곳을 미리 저장해두기
    m.append(data)
temp = [[0] * M for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

answer = 0
for c in combinations(cands, 3):
    for x, y in c:
        m[x][y] = 1

    # 임시 리스트에 원본을 복사
    for i in range(N):
        for j in range(M):
            temp[i][j] = m[i][j]

    # 바이러스가 있는 좌표부터 바이러스 확장
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                spread_v(i, j)

    # 0의 개수를 세기
    answer = max(answer, area_sum())

    # 벽을 세웠던 곳을 원상 복구
    for x, y in c:
        m[x][y] = 0
print(answer)
