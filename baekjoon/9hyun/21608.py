import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


def search_loc(x, favs):
    l_dict = dict()
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                continue
            if (i, j) not in l_dict:
                l_dict[(i, j)] = [0, 0]

            for d in direc:
                ni, nj = i + d[0], j + d[1]
                if in_range(ni, nj):
                    if graph[ni][nj] != 0:
                        if graph[ni][nj] in favs:  # 선호 학생 인접칸 카운트
                            l_dict[(i, j)][0] += 1
                    else:  # 빈 칸 카운트
                        l_dict[(i, j)][1] += 1

    locs = sorted(l_dict.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))  # 인접 칸 수, 빈 칸 수, 행렬번호 정렬
    sx, sy = locs[0][0]
    graph[sx][sy] = x


direc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
N = int(input())
graph = [[0] * N for _ in range(N)]


fav_data = dict()
for _ in range(N ** 2):
    data = list(map(int, input().split()))
    search_loc(data[0], data[1:])
    fav_data[data[0]] = data[1:]

answer = 0
for i in range(N):
    for j in range(N):
        x = graph[i][j]
        fav_score = 0
        for d in direc:
            ni, nj = i + d[0], j + d[1]
            if in_range(ni, nj):
                if graph[ni][nj] in fav_data[x]:
                    fav_score += 1

        if fav_score == 1:
            answer += 1
        elif fav_score == 2:
            answer += 10
        elif fav_score == 3:
            answer += 100
        elif fav_score == 4:
            answer += 1000
print(answer)