from copy import deepcopy
from collections import deque


def fish_move(graph_arg, sharkx, sharky):
    for num in range(1, 16 + 1):
        fish = find_fish(graph_arg, num)
        if fish is not None:
            x, y = fish
            f_d = graph_arg[x][y][1]
            for i in range(8):
                nx, ny = x + direction[f_d][0], y + direction[f_d][1]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == sharkx and ny == sharky):
                        graph_arg[x][y][1] = f_d
                        graph_arg[nx][ny], graph_arg[x][y] = graph_arg[x][y], graph_arg[nx][ny]
                        break
                f_d = (f_d + 1) % 8
    return graph_arg


def find_fish(graph_arg, num):
    for i in range(4):
        for j in range(4):
            if graph_arg[i][j][0] == num:
                return (i, j)
    return None


direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
graph = []
for i in range(4):
    data = list(map(int, input().split()))
    row = []
    for j in range(0, 8, 2):
        fish = [data[j], data[j + 1] - 1]
        row.append(fish)
    graph.append(row)


answer = 0
q = deque()
q.append([deepcopy(graph), (0, 0), graph[0][0][1], 0])
while q:
    graph_now, shark, s_d, count = q.popleft()
    sx, sy = shark

    graph_now[sx][sy][0] = -1
    answer = max(answer, count)

    # 물고기 움직이기
    graph_moved = fish_move(graph_now, sx, sy)

    # 상어 움직이기
    for i in range(4):
        sx += direction[s_d][0]
        sy += direction[s_d][1]
        if 0 <= sx < 4 and 0 <= sy < 4:
            if graph_moved[sx][sy][0] != -1:
                graph_temp = deepcopy(graph_moved)
                q.append([graph_temp, (sx, sy), graph_moved[sx][sy][1], count + graph_moved[sx][sy][0]])
        else:
            break
print(answer)