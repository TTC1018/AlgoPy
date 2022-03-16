from itertools import combinations
INF = int(1e9)


def calc_dist(combination):
    distance = 0
    for h in house:
        temp_dist = INF
        for k in combination: # 존재하는 치킨집 중에서 가장 가까운 위치까지의 거리
            temp_dist = min(temp_dist, abs(h[0] - k[0]) + abs(h[1] - k[1]))
        distance += temp_dist # 도시의 치킨거리에 기록
    return distance


N, M = map(int, input().split())
city, kfc, house = [], [], []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            kfc.append((i, j))
        elif row[j] == 1:
            house.append((i, j))
    city.append(row)

answer = INF
for c in combinations(kfc, M): # 살릴 수 있는 구성
    answer = min(answer, calc_dist(c))
print(answer)