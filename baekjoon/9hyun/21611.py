direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 소용돌이 그래프로 바꾸기
s_graph = []
g_direc = [(0, -1), (1, 0), (0, 1), (-1, 0)]
g_type = 1
g_idx = 0
g_d = 0
gx, gy = N // 2, N // 2
graph[gx][gy] = -1
while graph[gx][gy] != 0:
    for _ in range(g_type):
        gx, gy = gx + g_direc[g_d][0], gy + g_direc[g_d][1]
        if graph[gx][gy] == 0:
            break
        s_graph.append(graph[gx][gy])
    g_d = (g_d + 1) % 4
    g_idx += 1

    if g_idx == 2:
        g_idx = 0
        g_type += 1

# 파괴
for _ in range(M):
    d, s = map(int, input().split())
    d -= 1

    # 구슬 파괴
    g_len = len(graph)
    for i in range(s, 0, -1):
        rmv = pos + direc[d][0] * i * N + direc[d][1] * i
        if rmv < g_len:
            del graph[rmv]

    break
