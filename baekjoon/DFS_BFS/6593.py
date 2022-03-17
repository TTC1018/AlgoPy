from collections import deque

INF = int(1e9)

direction = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    S, E = tuple(), tuple()
    for i in range(L):
        stair = []
        for j in range(R):
            row = list(input())
            for k in range(C):
                if row[k] == 'S':
                    S = (i, j, k)
                elif row[k] == 'E':
                    E = (i, j, k)
            stair.append(row)
        building.append(stair)
        _ = input()

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[S[0]][S[1]][S[2]] = True

    q = deque()
    q.append(S + (0, ))
    answer = INF
    while q:
        s, x, y, count = q.popleft()
        if s == E[0] and x == E[1] and y == E[2]:
            answer = min(answer, count)
            continue

        for d in direction:
            ns, nx, ny = s + d[0], x + d[1], y + d[2]
            if 0 <= ns < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[ns][nx][ny]:
                    visited[ns][nx][ny] = True
                    if building[ns][nx][ny] != '#':
                        q.append((ns, nx, ny, count + 1))
    if answer == INF:
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).'.format(answer))