from collections import deque


M, N = map(int, input().split(' ')) # 열, 행
room = []
for i in range(N):
    room.append(list(map(int, list(input()))))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append((0, 0, 0))

answer = (N-1) + (M-1) - 1
while q:
    x, y, count = q.popleft()

    if x == M-1 and y == N-1:
        answer = min(answer, count)
        continue

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < M and 0 <= new_y < N:
            if room[new_y][new_x] == 1:
                q.append((new_x, new_y, count + 1))
            else:
                q.append((new_x, new_y, count))
print(answer)