import sys
from itertools import combinations

N, M = map(int, input().split())
C = []
P = []
H = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            H.append((i, j))
        elif temp[j] == 2:
            P.append((i, j))
    C.append(temp)

# 0: 빈 칸, 1: 집, 2: 치킨집
# 1 <= 집 <= 2N, M <= 치킨집 <= 13
# M개를 남길 때, 도시 치킨 거리의 최솟값
# 도시 치킨 거리 = 각 집이 갖는 치킨 거리의 합

distance = sys.maxsize
for c in combinations(P, M):
    temp_distance = 0
    for x, y in H:
        dist = sys.maxsize
        for rx, ry in c:
            dist = min(abs(x - rx) + abs(y - ry), dist)
        temp_distance += dist
    distance = min(temp_distance, distance)
print(distance)