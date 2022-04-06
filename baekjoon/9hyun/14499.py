def roll(loc, direction):
    nx, ny = loc
    
    if direction == 1: # 동
        tail = dice[1].pop()
        dice[1].insert(0, dice[-1])
        dice[-1] = tail
    elif direction == 2: # 서
        tail = dice[1].pop(0)
        dice[1].append(dice[-1])
        dice[-1] = tail
    elif direction == 3: # 북
        n_v = [dice[1][1], dice[2], dice[3], dice[0]]
        dice[0], dice[1][1], dice[2], dice[3] = n_v
    elif direction == 4: # 남
        n_v = [dice[3], dice[0], dice[1][1], dice[2]]
        dice[0], dice[1][1], dice[2], dice[3] = n_v
    
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[-1]
    else:
        graph[nx][ny], dice[-1] = 0, graph[nx][ny]
    print(dice[1][1])


N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0, [0, 0, 0], 0, 0]

for o in order:
    nx, ny = x + d[o - 1][0], y + d[o - 1][1]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        roll((x, y), o)