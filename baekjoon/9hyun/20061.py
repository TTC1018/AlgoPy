import sys
input = sys.stdin.readline

# 파란칸 밀기
def push_right(num):
    global blue

    blue = list(map(list, zip(*blue))) # pop 하기 쉽게 행과 열 뒤집기
    for _ in range(num):
        blue.pop()
    for _ in range(num):
        blue.insert(0, [False for _ in range(4)])
    blue = list(map(list, zip(*blue)))

# 초록칸 밀기
def push_down(num):
    for _ in range(num):
        green.pop()
    for _ in range(num):
        green.insert(0, [False for _ in range(4)])

# 밝은칸 체크
def check_light_b():
    checked = 0
    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                checked += 1
                break
    return checked


def check_light_g():
    checked = 0
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                checked += 1
                break
    return checked

# 가능한 지점까지 밀기
def push_b1(x):
    bx, by = x, 0
    while by < 6 and not blue[bx][by]:
        by += 1
    by -= 1
    blue[bx][by] = True
    return bx, by


def calc_b_col(by):
    global blue
    for i in range(4):
        if not blue[i][by]:
            return 0
    else:
        # 열 지우기
        blue = list(map(list, zip(*blue)))
        blue.pop(by)
        blue.insert(0, [False for _ in range(4)])
        blue = list(map(list, zip(*blue)))
        return 1

def push_g1(y):
    gx, gy = 0, y
    while gx < 6 and not green[gx][gy]:
        gx += 1
    gx -= 1
    green[gx][gy] = True
    return gx, gy


def calc_g_row(gx):
    for j in range(4):
        if not green[gx][j]:
            return 0
    else:
        # 행 밀기
        green.pop(gx)
        green.insert(0, [False for _ in range(4)])
        return 1

def put_block(t, x, y):
    if t == 1:
        bx, by = push_b1(x) # 파란 칸으로 진행
        gx, gy = push_g1(y) # 초록 칸으로 진행

        score = calc_b_col(by) + calc_g_row(gx) # 행, 열 지워서 만든 점수
        check_b = check_light_b() # 밝은 색 칸 확인
        check_g = check_light_g()
        if check_b >= 1:
            push_right(check_b)
        if check_g >= 1:
            push_down(check_g)

        return score
    elif t == 2:
        bx, by = push_b1(x) # 파란 칸 입장에서는 서있는 막대기
        blue[bx][by - 1] = True # 윗 블럭도 방문처리

        gx1, gy1 = push_g1(y)
        gx2, gy2 = push_g1(y + 1)

        # 높낮이 맞추기
        if gx1 < gx2:
            green[gx2][gy2] = False
            gx2 = gx1
            green[gx2][gy2] = True
        else:
            green[gx1][gy1] = False
            gx1 = gx2
            green[gx1][gy1] = True
        score = calc_b_col(by)
        if score == 0: # 맨 아랫줄 안 지워졌을 때
            score += calc_b_col(by - 1) # 그 윗 줄 지워보기
        else:
            score += calc_b_col(by) # 밀려 내려온 윗줄 지워보기
        score += calc_g_row(gx1)
        check_b = check_light_b()  # 밝은 색 칸 확인
        check_g = check_light_g()
        if check_b >= 1:
            push_right(check_b)
        if check_g >= 1:
            push_down(check_g)

        return score
    elif t == 3:
        gx, gy = push_g1(y)  # 초록 칸 입장에서 서있는 막대기
        green[gx - 1][gy] = True  # 윗 블럭도 방문처리

        bx1, by1 = push_b1(x)
        bx2, by2 = push_b1(x + 1)

        # 높낮이 맞추기
        if by1 < by2:
            blue[bx2][by2] = False
            by2 = by1
            blue[bx2][by2] = True
        else:
            blue[bx1][by1] = False
            by1 = by2
            blue[bx1][by1] = True
        score = calc_g_row(gx)
        if score == 0:  # 맨 아랫줄 안 지워졌을 때
            score += calc_g_row(gx - 1)  # 그 윗 줄 지워보기
        else:
            score += calc_g_row(gx)  # 밀려 내려온 윗줄 지워보기
        score += calc_b_col(by1)
        check_b = check_light_b()  # 밝은 색 칸 확인
        check_g = check_light_g()
        if check_b >= 1:
            push_right(check_b)
        if check_g >= 1:
            push_down(check_g)

        return score


blue = [[False] * 6 for _ in range(4)]
green = [[False] * 4 for _ in range(6)]
N = int(input())

score_val = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    score_val += put_block(t, x, y)

# 남은 블럭 세기
t_cnt = 0
for i in range(4):
    for j in range(6):
        if blue[i][j]:
            t_cnt += 1
for i in range(6):
    for j in range(4):
        if green[i][j]:
            t_cnt += 1
print(score_val)
print(t_cnt)