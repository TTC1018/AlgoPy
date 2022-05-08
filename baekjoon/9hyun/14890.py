import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


def go(x, y, d):
    global answer
    prev = graph[x][y]
    count = 1

    nx, ny = x, y
    for _ in range(N - 1):
        nx, ny = nx + direc[d][0], ny + direc[d][1]
        if graph[nx][ny] == prev:
            count += 1
        elif graph[nx][ny] == prev + 1: # 오르막이면
            if count >= L: # 경사로 공간 충분하면
                count = 1
                prev = graph[nx][ny]
            else:
                break
        elif graph[nx][ny] == prev - 1: # 내리막이면
            if count >= 0:
                count = -L + 1 # 내리막 경사로 카운트 하도록 음수로 변경
                prev = graph[nx][ny]
            else:
                break
        else: # 2 이상 차이날 때
            break
    else: # break 없이 다 돌았을 때
        if count >= 0:
            answer += 1


N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direc = [(0, 1), (1, 0)]
answer = 0
for i in range(N):
    go(i, 0, 0)
    go(0, i, 1)
print(answer)
