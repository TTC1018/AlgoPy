from itertools import combinations
from copy import deepcopy

N, M, D = map(int, input().split()) # 행 열 사정거리
grids = []
break_condition = [[0] * M for _ in range(N)]
for _ in range(N):
    grids.append(list(map(int, input().split())))

# 궁수 3명 고정 (위치는 자유)
# 사정거리 내에 여러 대상이 있다면 가장 왼쪽을 사격
# 두 좌표 간의 거리 = |x1 - x2| + |y1 - y2|
# 적은 가장 아래 행을 넘어서면 소멸
# 제거 가능한 최대수
def solve(rangers):
    grid_copy = deepcopy(grids)
    result = 0
    while grid_copy != break_condition:
        for ranger in rangers:
            flag = False
            for i in range(ranger - (D - 1), ranger + (D - 1) + 1):
                if flag:
                    break
                if 0 <= i < M:
                    for j in range(D - abs(ranger - i), -1, -1):
                        row = (N - 1) - j
                        if 0 <= row < N:
                            if grid_copy[row][i] == 1:
                                grid_copy[row][i] = 0
                                result += 1
                                flag = True
                                break
        grid_copy.pop(N - 1)
        grid_copy.insert(0, [0] * M)
    return result


answer = 0
for c in combinations([n for n in range(5)], 3):
    answer = max(answer, solve(c))
print(answer)