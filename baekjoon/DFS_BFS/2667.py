from collections import deque

N = int(input())

home = []
for i in range(N):
    home.append(list(map(int, input())))
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

q = deque()
answer = []
area = 1
for i in range(N):
    for j in range(N):
        if home[i][j] == 1:
            home[i][j] = 0
            q.append((i, j))
            temp_count = 1
            while q:
                now = q.popleft()
                x, y = now
                for d in direction:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if home[nx][ny] == 1:
                            home[nx][ny] = 0
                            q.append((nx, ny))
                            temp_count += 1
            answer.append(temp_count)
            area += 1

answer.sort()
print(len(answer))
for a in answer:
    print(a)