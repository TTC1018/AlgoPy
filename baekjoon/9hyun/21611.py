import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline


def transform():
    global s_graph
    if not s_graph: # 빈 그래프는 처리 할 필요 없음
        return

    limit = N * N - 1
    end = len(s_graph)

    prev = s_graph[0]
    i = 1
    b_cnt = 1
    new_graph = []
    while i < end:
        if prev == s_graph[i]:
            b_cnt += 1
        else:
            new_graph += [b_cnt, prev]
            b_cnt = 1
            prev = s_graph[i]
        i += 1
        if i == end:
            new_graph += [b_cnt, s_graph[-1]]

    if len(new_graph) > limit:
        new_graph = new_graph[:limit]
    return new_graph


def explode():
    global answer

    e_flag = False
    end = len(s_graph)

    prev = s_graph[0]
    i = 1
    b_cnt = 1
    while i < end:
        if prev == s_graph[i]:
            b_cnt += 1
        else:
            score = prev
            prev = s_graph[i]
            if b_cnt >= 4:
                del s_graph[i - b_cnt: i]
                e_flag = True
                answer += score * b_cnt
                i -= b_cnt
                end = len(s_graph)
            b_cnt = 1
        i += 1
        if i == end: # 마지막까지 연속되던 구슬 처리 안 하는 경우 방지
            if b_cnt >= 4:
                e_flag = True
                answer += s_graph[-1] * b_cnt
                del s_graph[end - b_cnt: end]
            break
    if e_flag and s_graph: # 빈 그래프는 더이상 처리 안 하기
        explode()


def destroy(b_info):
    d, s = b_info
    d -= 1
    for i in range(s, 0, -1): # pop 사용할 것이므로 뒤 인덱스부터 제거
        tx, ty = sx + i * direc[d][0], sy + i * direc[d][1]
        pos = pos_dict[(tx, ty)]
        if len(s_graph) > pos:
            s_graph.pop(pos)


direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
blizzard = [tuple(map(int, input().split())) for _ in range(M)]

# 소용돌이 그래프로 바꾸기
pos_dict = dict()
s_graph = []
g_direc = [(0, -1), (1, 0), (0, 1), (-1, 0)]
g_type, g_idx, g_d = 1, 0, 0
gx, gy = N // 2, N // 2 # 그래프 중앙
graph[gx][gy] = -1

idx_cnt = 0
# 나선 모양으로 돌며 기록
while gx >= 0 and gy >= 0:
    for _ in range(g_type):
        gx, gy = gx + g_direc[g_d][0], gy + g_direc[g_d][1]
        if graph[gx][gy] != 0:
            s_graph.append(graph[gx][gy])
        pos_dict[(gx, gy)] = idx_cnt
        idx_cnt += 1
    g_d = (g_d + 1) % 4
    g_idx += 1

    if g_idx == 2:
        g_idx = 0
        g_type += 1

answer = 0
sx, sy = N // 2, N // 2
for i in range(M):
    if not s_graph: # 빈 그래프면 처리 X
        break
    destroy(blizzard[i])
    explode()
    s_graph = transform()
print(answer)