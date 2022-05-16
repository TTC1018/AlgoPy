from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


def consecutive(x, y, val):
    q = deque()
    q.append((x, y))
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    cnt = 1
    while q:
        tx, ty = q.popleft()
        for d in direc:
            nx, ny = tx + d[0], ty + d[1]
            if in_range(nx, ny):
                if graph[nx][ny] == val and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))
    return cnt * val


def roll(x, y):
    if dice_d == 0: # 동쪽
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
        return x, y + 1
    elif dice_d == 1: # 남쪽
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
        return x + 1, y
    elif dice_d == 2: # 서쪽
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
        return x, y - 1
    elif dice_d == 3: # 북쪽
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
        return x - 1, y


direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dice = [2, 4, 1, 3, 5, 6]
dice_d = 0
dx, dy = 0, 0

answer = 0
for _ in range(K):
    nx, ny = dx + direc[dice_d][0], dy + direc[dice_d][1]
    if in_range(nx, ny): # 이동 가능
       dx, dy = roll(dx, dy)
    else: # 이동 불가 (방향 반대 전환)
        dice_d = direc.index((-direc[dice_d][0], -direc[dice_d][1]))
        dx, dy = roll(dx, dy)
    # 점수 획득 및 이동 방향 결정
    A, B = dice[5], graph[dx][dy] # 주사위 아랫면, 주사위가 있는 칸
    answer += consecutive(dx, dy, B)
    if A > B:
        dice_d = (dice_d + 1) % 4
    elif A < B:
        dice_d = (dice_d - 1) % 4

print(answer)