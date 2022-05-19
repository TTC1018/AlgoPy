from collections import deque

def transpose(rubik):
    rubik = [list(r) for r in rubik]
    rubik = list(map(list, zip(*rubik)))  # 행,열 뒤집기
    rubik = list(map(deque, rubik))
    return rubik


def clock_spin(rubik):
    rubik = [list(r) for r in rubik]
    rubik = list(map(list, zip(*rubik)))
    for i in range(3):
        rubik[i].reverse()
    rubik = list(map(deque, rubik))
    return rubik

def c_clock_spin(rubik):
    rubik = [list(r) for r in rubik]
    rubik = list(map(list, zip(*rubik)))
    rubik.reverse()
    rubik = list(map(deque, rubik))
    return rubik



def clock(part):
    global rubik_left, rubik_right, rubik_front, rubik_back, rubik_down, rubik_up

    if part in ['U', 'D']:
        idx = 0 if part == 'U' else 2
        if idx == 0:
            rubik_up = clock_spin(rubik_up)
            for _ in range(3):
                rubik_left[idx].append(rubik_front[idx].popleft())
            for _ in range(3):
                rubik_back[idx].append(rubik_left[idx].popleft())
            for _ in range(3):
                rubik_right[idx].append(rubik_back[idx].popleft())
            for _ in range(3):
                rubik_front[idx].append(rubik_right[idx].popleft())
        elif idx == 2:
            rubik_down = clock_spin(rubik_down)
            for _ in range(3):
                rubik_right[idx].appendleft(rubik_front[idx].pop())
            for _ in range(3):
                rubik_back[idx].appendleft(rubik_right[idx].pop())
            for _ in range(3):
                rubik_left[idx].appendleft(rubik_back[idx].pop())
            for _ in range(3):
                rubik_front[idx].appendleft(rubik_left[idx].pop())
    elif part in ['L', 'R']:
        idx = 0 if part == 'L' else 2
        rubik_up = clock_spin(rubik_up)  # 행,열 뒤집기
        rubik_front = clock_spin(rubik_front)
        rubik_down = clock_spin(rubik_down)
        rubik_back = clock_spin(rubik_back)
        if idx == 0:
            rubik_left = clock_spin(rubik_left)
            for _ in range(3):
                rubik_up[idx].append(rubik_back[idx].popleft())
            for _ in range(3):
                rubik_front[idx].append(rubik_up[idx].popleft())
            for _ in range(3):
                rubik_down[idx].append(rubik_front[idx].popleft())
            for _ in range(3):
                rubik_back[idx].append(rubik_down[idx].popleft())
        elif idx == 2:
            rubik_right = clock_spin(rubik_right)
            for _ in range(3):
                rubik_back[idx].appendleft(rubik_up[idx].pop())
            for _ in range(3):
                rubik_down[idx].appendleft(rubik_back[idx].pop())
            for _ in range(3):
                rubik_front[idx].appendleft(rubik_down[idx].pop())
            for _ in range(3):
                rubik_up[idx].appendleft(rubik_front[idx].pop())
        rubik_up = transpose(rubik_up)
        rubik_front = transpose(rubik_front)
        rubik_down = transpose(rubik_down)
        rubik_back = transpose(rubik_back)
    elif part in ['F', 'B']:
        idx = 0 if part == 'B' else 2
        if idx == 0:
            rubik_back = clock_spin(rubik_back)
            for _ in range(3):
                rubik_left[idx].append(rubik_up[idx].popleft())
            for _ in range(3):
                rubik_down[idx].append(rubik_left[idx].popleft())
            for _ in range(3):
                rubik_right[idx].append(rubik_down[idx].popleft())
            for _ in range(3):
                rubik_up[idx].append(rubik_right[idx].popleft())
        elif idx == 2:
            rubik_front = clock_spin(rubik_front)
            for _ in range(3):
                rubik_right[idx].appendleft(rubik_up[idx].pop())
            for _ in range(3):
                rubik_down[idx].appendleft(rubik_right[idx].pop())
            for _ in range(3):
                rubik_left[idx].appendleft(rubik_down[idx].pop())
            for _ in range(3):
                rubik_up[idx].appendleft(rubik_left[idx].pop())


def counterclock(part):
    global rubik_left, rubik_right, rubik_front, rubik_back, rubik_down, rubik_up

    if part in ['U', 'D']:
        idx = 0 if part == 'U' else 2
        if idx == 0:
            rubik_up = c_clock_spin(rubik_up)
            for _ in range(3):
                rubik_right[idx].appendleft(rubik_front[idx].pop())
            for _ in range(3):
                rubik_back[idx].appendleft(rubik_right[idx].pop())
            for _ in range(3):
                rubik_left[idx].appendleft(rubik_back[idx].pop())
            for _ in range(3):
                rubik_front[idx].appendleft(rubik_left[idx].pop())
        elif idx == 2:
            rubik_down = c_clock_spin(rubik_down)
            for _ in range(3):
                rubik_left[idx].append(rubik_front[idx].popleft())
            for _ in range(3):
                rubik_back[idx].append(rubik_left[idx].popleft())
            for _ in range(3):
                rubik_right[idx].append(rubik_back[idx].popleft())
            for _ in range(3):
                rubik_front[idx].append(rubik_right[idx].popleft())
    elif part in ['L', 'R']:
        idx = 0 if part == 'L' else 2
        rubik_up = transpose(rubik_up) # 행,열 뒤집기
        rubik_front = transpose(rubik_front)
        rubik_down = transpose(rubik_down)
        rubik_back = transpose(rubik_back)
        if idx == 0:
            rubik_left = c_clock_spin(rubik_left)
            for _ in range(3):
                rubik_down[idx].appendleft(rubik_back[idx].pop())
            for _ in range(3):
                rubik_front[idx].appendleft(rubik_down[idx].pop())
            for _ in range(3):
                rubik_up[idx].appendleft(rubik_front[idx].pop())
            for _ in range(3):
                rubik_back[idx].appendleft(rubik_up[idx].pop())
        elif idx == 2:
            rubik_right = c_clock_spin(rubik_right)
            for _ in range(3):
                rubik_front[idx].append(rubik_up[idx].popleft())
            for _ in range(3):
                rubik_down[idx].append(rubik_front[idx].popleft())
            for _ in range(3):
                rubik_back[idx].append(rubik_down[idx].popleft())
            for _ in range(3):
                rubik_up[idx].append(rubik_back[idx].popleft())
        rubik_up = transpose(rubik_up)
        rubik_front = transpose(rubik_front)
        rubik_down = transpose(rubik_down)
        rubik_back = transpose(rubik_back)
    elif part in ['F', 'B']:
        idx = 0 if part == 'B' else 2
        if idx == 0:
            rubik_back = c_clock_spin(rubik_back)
            for _ in range(3):
                rubik_right[idx].appendleft(rubik_up[idx].pop())
            for _ in range(3):
                rubik_down[idx].appendleft(rubik_right[idx].pop())
            for _ in range(3):
                rubik_left[idx].appendleft(rubik_down[idx].pop())
            for _ in range(3):
                rubik_up[idx].appendleft(rubik_left[idx].pop())
        elif idx == 2:
            rubik_front = c_clock_spin(rubik_front)
            for _ in range(3):
                rubik_left[idx].append(rubik_up[idx].popleft())
            for _ in range(3):
                rubik_down[idx].append(rubik_left[idx].popleft())
            for _ in range(3):
                rubik_right[idx].append(rubik_down[idx].popleft())
            for _ in range(3):
                rubik_up[idx].append(rubik_right[idx].popleft())

def rotate(part, direc):
    if direc == '+':
        clock(part)
    else:
        counterclock(part)


for _ in range(int(input())):
    rubik_up = [deque(['w' for _ in range(3)]) for _ in range(3)]
    rubik_left = [deque(['g' for _ in range(3)]) for _ in range(3)]
    rubik_right = [deque(['b' for _ in range(3)]) for _ in range(3)]
    rubik_front = [deque(['r' for _ in range(3)]) for _ in range(3)]
    rubik_back = [deque(['o' for _ in range(3)]) for _ in range(3)]
    rubik_down = [deque(['y' for _ in range(3)]) for _ in range(3)]

    n = int(input())
    spin = input().split()

    for s in spin:
        rotate(s[0], s[1])
        for r in rubik_back:
            print(''.join(r))

    # for r in rubik_up:
    #     print(''.join(r))