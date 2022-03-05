from collections import deque


def answer():
    result = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            result += graph[i][j]
    return result


def move_cloud(d_index):
    c_len = len(cloud)

    for i in range(c_len):
        x, y = cloud.popleft()
        nx, ny = x + direction[d_index][0], y + direction[d_index][1]
        if nx < 1:
            nx = N
        elif nx > N:
            nx %= N
        if ny < 1:
            ny = N
        elif ny > N:
            ny %= N
        cloud.append((nx, ny))


def raining():
    for c in cloud:
        x, y = c
        graph[x][y] += 1


c_water_direc = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
def copy_water():
    for c in cloud:
        x, y = c
        count = 0
        for c_w_d in c_water_direc:
            tx, ty = x + c_w_d[0], y + c_w_d[1]
            if 1 <= tx <= N and 1 <= ty <= N:
                if graph[tx][ty] > 0:
                    count += 1
        graph[x][y] += count


def generate_cloud():

    exceptions = []
    while cloud:
        exceptions.append(cloud.popleft())

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] >= 2 and (i, j) not in exceptions:
                cloud.append((i, j))
                graph[i][j] -= 2


N, M = map(int, input().split())

graph = [[]]
for i in range(N):
    graph.append([0] + list(map(int, input().split())))
order = [tuple(map(int, input().split())) for _ in range(M)]
cloud = deque()
cloud.append((N, 1))
cloud.append((N, 2))
cloud.append((N - 1, 1))
cloud.append((N - 1, 2))

# 1: (0, -1), 2: (-1, -1), 3: (-1, 0)
# 4: (-1, 1), 5: (0, 1), 6: (1, 1)
# 7: (1, 0), 8: (1, -1)
direction = [(0, 0),
             (0, -1), (-1, -1), (-1, 0),
             (-1, 1), (0, 1), (1, 1),
             (1, 0), (1, -1)]
# 1. di 방향으로 s칸 이동
# 2. 도착지에 물의 양 1 증가
# 3. 구름 제거
# 4. 대각선에 물 있는 개수만큼 물 증가
# 5. 물의 양이 2 이상이면 구름이 생기고 물 2 줄어듦 (이전 도착 위치에 중복 구름 생성은 x)


for o in order:
    o_d, o_s = o
    for _ in range(o_s):
        move_cloud(o_d)
    raining()
    copy_water()
    generate_cloud()
print(answer())