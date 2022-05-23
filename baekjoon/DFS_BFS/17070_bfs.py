from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


direc = [(0, 1), (1, 1), (1, 0)]
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
if graph[N - 1][N - 1]:
    print(0)
    sys.exit()

q = deque()
q.append((0, 1, 0))
answer = 0
while q:
    x, y, prev_d = q.popleft()
    if (x, y) == (N - 1, N - 1):
        answer += 1
        continue


    for i in range(3):
        nx, ny = x + direc[i][0], y + direc[i][1]
        if in_range(nx, ny) and not graph[nx][ny]:
            if i == 1:
                if not graph[nx - 1][ny] and not graph[nx][ny - 1]:
                    q.append((nx, ny, i))
            else:
                if prev_d in [i, 1]:
                    q.append((nx, ny, i))
print(answer)