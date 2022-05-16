from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < 2**N and 0 <= y < 2**N


def solve():
    # 남은 얼음 합
    ice_sum = 0
    for i in range(2**N):
        for j in range(2**N):
            if graph[i][j] > 0:
                ice_sum += graph[i][j]
    print(ice_sum)

    # 덩어리 칸 세기
    answers = []
    visited = [[False] * (2**N) for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            if graph[i][j] > 0:
                visited[i][j] = True
                q = deque()
                q.append((i, j))

                i_cnt = 1
                while q:
                    x, y = q.popleft()
                    for d in direc:
                        nx, ny = x + d[0], y + d[1]
                        if in_range(nx, ny):
                            if not visited[nx][ny] and graph[nx][ny] > 0:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                i_cnt += 1
                answers.append(i_cnt)

    answers.sort()
    if len(answers) > 0:
        print(answers[-1])
    else:
        print(0)


def melt():
    nxt = [[False] * 2**N for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for d in direc:
                ni, nj = i + d[0], j + d[1]
                if in_range(ni, nj):
                    if graph[ni][nj] > 0:
                        cnt += 1
            if cnt < 3:
                nxt[i][j] = True

    for i in range(2**N):
        for j in range(2**N):
            if nxt[i][j]:
                graph[i][j] -= 1

def turn(x, y, l):
    part = []
    for i in range(2**l):
        part.append(graph[x + i][y:y + 2**l])

    part = list(map(list, zip(*part)))
    for i in range(2**l):
        for j in range(2**l):
            graph[x + i][y + j] = part[i][2**l - 1 - j]



def firestorm(l):
    if l > 0:
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                turn(i, j, l)
    melt()


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, Q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2**N)]
# graph = [[i*2**N+j for j in range(2**N)] for i in range(2**N)]
L = list(map(int, input().split()))

for level in L:
    firestorm(level)
solve()