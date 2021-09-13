from collections import deque
from copy import deepcopy

N, M, D = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
data.append([0] * M)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 궁수가 공격하는 적은 거리가 D 이하인 적 중 가장 가까운 적

# 적이 하나도 없는지 확인 (있으면 False 리턴)
def check(data):
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                return False
    return True


# 거리가 D이하인 적 중에서 가장 가까운 적 위치 반환
def bfs(x, y, data):
    q = deque()
    q.append((x, y))
    check = {(x, y): 1}
    point = []
    nq = deque()
    distance = 0
    while 1:
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and check.get((nx, ny)) is None:
                    check[(nx, ny)] = 1
                    if data[nx][ny] == 1:
                        point.append((nx, ny))
                    else:
                        nq.append((nx, ny))

        distance += 1
        if distance > D:
            return -1, -1

        if point:
            if len(point) > 1:
                point = sorted(point, key=lambda x: x[1])
            return point[0][0], point[0][1]
        else:
            q = nq
            nq = deque()


# 제거한 적의 개수 반환
def remove_enemy_count(data):
    count = 0
    while 1:
        # 공격하고
        enemy = set()
        for j in range(M):
            if data[N][j] == 2:
                e_x, e_y = bfs(N, j, data)
                if e_x != -1:
                    enemy.add((e_x, e_y))
        count += len(enemy)
        for x, y in enemy:
            data[x][y] = 0

        # 적이 이동
        for i in range(N - 1, -1, -1):
            for j in range(M):
                if data[i][j] == 1:
                    data[i][j] = 0
                    if i != (N - 1):
                        data[i + 1][j] = 1
        if check(data):
            return count


answer = 0
# 궁수 3명 배치 함수
def solve(count, data):
    global answer
    if count == 3:
        data = deepcopy(data)
        answer = max(answer, remove_enemy_count(data))
        return

    for i in range(M):
        if data[N][i] == 0:
            data[N][i] = 2
            solve(count + 1, data)
            data[N][i] = 0


solve(0, data)
print(answer)