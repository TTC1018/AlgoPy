def zero_check(temp_key):
    for r in temp_key:
        for c in r:
            if c != 0:
                return False
    return True


def unlock_check(temp_key):
    for t in t_loc:
        if temp_key[t[0]][t[1]] != 1:
            return False

    length = len(temp_key[0])
    for i in range(length):
        for j in range(length):
            if (i, j) not in t_loc and temp_key[i][j] == 1:
                return False
    return True


def clock_rot(temp_key):
    length = len(temp_key[0])
    rotated = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            rotated[i][j] = temp_key[length - 1 - j][i]
    return rotated


def counter_clock_rot(temp_key):
    length = len(temp_key[0])
    rotated = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            rotated[i][j] = temp_key[j][length - 1 - i]
    return rotated


def left_rot(temp_key):
    length = len(temp_key[0])
    rotated = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length - 1):
            rotated[i][j] = temp_key[i][j + 1]
    return rotated


def right_rot(temp_key):
    length = len(temp_key[0])
    rotated = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(1, length):
            rotated[i][j] = temp_key[i][j - 1]
    return rotated


def up_rot(temp_key):
    length = len(temp_key[0])
    rotated = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length - 1):
        for j in range(length):
            rotated[i][j] = temp_key[i + 1][j]
    return rotated


def down_rot(temp_key):
    length = len(temp_key[0])
    rotated = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(1, length):
        for j in range(length):
            rotated[i][j] = temp_key[i - 1][j]
    return rotated


def same_check(origin, temp_key):
    length = len(temp_key)
    for i in range(length):
        for j in range(length):
            if origin[i][j] != temp_key[i][j]:
                return False
    return True


def checking(origin, temp_key):
    global answer

    if answer:
        return

    if zero_check(temp_key):
        answer = False
        return

    if unlock_check(temp_key):
        answer = True
        return

    for f in functions:
        rotated = f(temp_key)
        if not same_check(origin, rotated):
            checking(origin, rotated)


def solution(key, lock):
    # lock이 전부 0이고 key가 전부 1인지 확인
    if zero_check(lock):
        isAllOne = True
        for r in key:
            for c in r:
                if c != 1:
                    isAllOne = False
        if isAllOne:
            return True

    # Lock에서 0 위치 찾기
    length = len(lock[0])
    for i in range(length):
        for j in range(length):
            if lock[i][j] == 0:
                t_loc.append((i, j))

    # 가능한 경우의 수 만들어 내서 체크
    checking(key, key)
    return answer


t_loc = []
functions = [up_rot, down_rot, clock_rot, counter_clock_rot, left_rot, right_rot]
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
answer = False
print(solution(key, lock))