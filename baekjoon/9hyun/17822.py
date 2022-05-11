from collections import deque
import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < M


def spin(num, d_val, k_val):
    if d_val == 0: # 시계
        for _ in range(k_val):
            board[num].appendleft(board[num].pop())
    else: # 반시계
        for _ in range(k_val):
            board[num].append(board[num].popleft())


def erase():
    cand = set()

    for i in range(N):
        for j in range(M):
            for d in direc:
                nx, ny = i + d[0], j + d[1]
                if ny == -1: # in_range 벗어나지 않게 재조정
                    ny = M - 1
                elif ny == M:
                    ny = 0

                if in_range(nx, ny):
                    if board[i][j] > 0:
                        if board[i][j] == board[nx][ny]:
                            cand.add((nx, ny))
                            cand.add((i, j))

    if len(cand) == 0: # 지워진 수 없을 때
        # 평균 구하기
        total, count = 0, 0 # 전체 합 / 0 개수 (지워진 수)
        for b in board:
            total += sum(b)
            count += b.count(0)

        if count == N * M: # 이미 다 지워졌을 때
            return

        average = total / (N * M - count)
        for i in range(N):
            for j in range(M):
                if board[i][j] > 0:
                    if board[i][j] > average:
                        board[i][j] -= 1
                    elif board[i][j] < average:
                        board[i][j] += 1
    else: # 지워야 할 수 있을 때
        for x, y in cand:
            board[x][y] = 0 # 0으로 지움 처리


direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M, T = map(int, input().split())
board = [deque(list(map(int, input().split()))) for _ in range(N)]
for _ in range(T):
    x, d, k = map(int, input().split()) # x의 배수인 원판을 d 방향으로 k칸 회전
    for i in range(1, N + 1):
        if i % x == 0:
            spin(i - 1, d, k)
    erase()

answer = 0
for b in board:
    answer += sum(b)
print(answer)