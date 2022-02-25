def clock_rot(temp_key):
    length = len(temp_key[0])
    rotated = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            rotated[i][j] = temp_key[length - 1 - j][i]
    return rotated


def is_solved(lock):
    length = len(lock[0]) // 3
    for i in range(length, length + length): # 확장된 자물쇠의 중앙만 확인
        for j in range(length, length + length):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    M = len(key[0])
    N = len(lock[0])

    expanded_lock = [[0] * (N * 3) for _ in range(N * 3)] # 열쇠를 쉽게 확인해보기 위해 자물쇠를 크게 늘림
    for i in range(N):
        for j in range(N):
            expanded_lock[i + N][j + N] = lock[i][j] # 가운데 영역이 원래 자물쇠

    for _ in range(4):
        key = clock_rot(key)
        for x in range(N + 1 - M, N * 2):
            for y in range(N + 1 - M, N * 2):
                for i in range(M):
                    for j in range(M):
                        expanded_lock[x + i][y + j] += key[i][j]

                if is_solved(expanded_lock): # 열쇠를 끼웠을 때 자물쇠 영역이 전부 1인지 확인
                    return True

                for i in range(M):
                    for j in range(M):
                        expanded_lock[x + i][y + j] -= key[i][j] # 원상복구
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))