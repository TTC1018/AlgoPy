import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x < N and 0 <= y < N


def push(x, y, d):
    global answer
    if (x, y) == (0, 0): # 도착지점이면 끝
        return x, y

    sx, sy = x + direc[d][0], y + direc[d][1]
    sand = A[sx][sy]
    rest = sand
    
    # a 제외 나머지 비율만큼 더하기
    for target in wind[d]:
        tx, ty, rate = target
        seper = int(sand * rate)
        if in_range(x + tx, y + ty):
            A[x + tx][y + ty] += seper
        else:
            answer += seper
        rest -= seper
    
    # a에 남은 모래 옮기기
    ax, ay = x + direc[d][0] * 2, y + direc[d][1] * 2
    if in_range(ax, ay):
        A[ax][ay] += rest
    else:
        answer += rest
    
    # y자리 비우기
    A[sx][sy] = 0
    
    return sx, sy



left = [(0, -3, 0.05), (-1, -2, 0.1), (1, -2, 0.1),
        (-1, -1, 0.07), (1, -1, 0.07), (-2, -1, 0.02),
        (2, -1, 0.02), (-1, 0, 0.01), (1, 0, 0.01)]
right = [(x, -y, z) for (x, y, z) in left]
up = [(y, x, z) for (x, y, z) in left]
down = [(-x, y, z) for (x, y, z) in up]
wind = [left, down, right, up]

direc = [(0, -1), (1, 0), (0, 1), (-1, 0)]
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

X, Y = N // 2, N // 2
t_idx = 1 # 2번마다 증가함
t_cnt = 0 # 횟수 카운트 (2번마다 초기화)
d_idx = 0 # 방향 인덱스

answer = 0
while (X, Y) != (0, 0): # 도착지점까지 진행
    for _ in range(t_idx):
        X, Y = push(X, Y, d_idx)
    d_idx = (d_idx + 1) % 4
    t_cnt += 1
    if t_cnt == 2:
        t_idx += 1
        t_cnt = 0
print(answer)