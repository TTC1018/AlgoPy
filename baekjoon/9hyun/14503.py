import sys
input = sys.stdin.readline


def clean(x, y, now_d):
    global answer
    if not visited[x][y]:
        visited[x][y] = True
        answer += 1

    left = now_d - 1 if now_d != 0 else 3
    lx, ly = x + direc[left][0], y + direc[left][1]
    if not graph[lx][ly] and not visited[lx][ly]:
        return lx, ly, left, True
    else:
        return x, y, left, False


direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
b_cnt = 0

answer = 0
while True:
    r, c, d, back_to_first = clean(r, c, d)
    if not back_to_first:
        b_cnt += 1
        if b_cnt == 4:
            # 후진 시도
            bx, by = r - direc[d][0], c - direc[d][1]
            if graph[bx][by]: # 벽이면
                break
            else:
                r, c = bx, by
                b_cnt = 0
    else:
        b_cnt = 0
print(answer)