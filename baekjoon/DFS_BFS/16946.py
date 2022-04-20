import sys
from collections import deque
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


def search_area(x, y, area_num):
    count = 1
    q.append((x, y))
    while q:
        i, j = q.popleft()
        for d in direc:
            ni, nj = i + d[0], j + d[1]
            if in_range(ni, nj):
                if graph[ni][nj] == 0:
                    graph[ni][nj] = area_num
                    q.append((ni, nj))
                    count += 1
    return count


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
answer = [[0] * M for _ in range(N)]
q = deque()
# 0 = 이동 가능, 1 = 벽
# 원래 빈 칸이면 0 출력, 벽이면 이동가능 칸 개수 10으로 나눈 나머지
area_num = 2
area = dict()

# 구역 기록하기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            graph[i][j] = area_num
            area[area_num] = search_area(i, j, area_num)
            area_num += 1

# 이동 구역 세기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            answer[i][j] = 1
            cand = set()
            for d in direc:
                ni, nj = i + d[0], j + d[1]
                if in_range(ni, nj) and graph[ni][nj] != 1:
                    cand.add(graph[ni][nj])
            for c in cand:
                answer[i][j] += area[c]
            answer[i][j] %= 10
            

for a in answer:
    print(*a, sep="")