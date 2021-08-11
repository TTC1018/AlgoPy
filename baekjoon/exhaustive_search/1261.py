from collections import deque


M, N = map(int, input().split(' ')) # 열, 행
room = []
for i in range(N):
    room.append(list(map(int, list(input()))))

# 상하좌우
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

q = deque()
q.append((0, 0, 0))

visited = [[False] * M for _ in range(N)]
visited[0][0] = True
answer = (N-1) + (M-1) - 1

while q:
    x, y, count = q.popleft()

    if x == M-1 and y == N-1:
        answer = count
        break

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < M and 0 <= new_y < N:
            if not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                if room[new_y][new_x] == 0:
                    q.appendleft((new_x, new_y, count)) # 저비용 우선 탐색
                else:
                    q.append((new_x, new_y, count + 1))
print(answer)