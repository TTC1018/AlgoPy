def clock_rot(temp_key):
    length = len(temp_key[0])
    rotated = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            rotated[i][j] = temp_key[length - 1 - j][i]
    return rotated


def is_solved(lock):
    length = len(lock[0]) // 3
    for i in range(length, length + length):
        for j in range(length, length + length):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    M = len(key[0])
    N = len(lock[0])

    expanded_lock = [[0] * (N * 3) for _ in range(N * 3)]
    for i in range(N):
        for j in range(N):
            expanded_lock[i + N][j + N] = lock[i][j]

    for _ in range(4):
        key = clock_rot(key)
        for x in range(N * 2):
            for y in range(N * 2):
                for i in range(M):
                    for j in range(M):
                        expanded_lock[x + i][y + j] += key[i][j]

                if is_solved(expanded_lock):
                    return True

                for i in range(M):
                    for j in range(M):
                        expanded_lock[x + i][y + j] -= key[i][j]
    return False