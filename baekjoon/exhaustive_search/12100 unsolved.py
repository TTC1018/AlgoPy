from collections import deque
from copy import deepcopy

N = int(input())
B = []
for i in range(N):
    B.append(list(map(int, input().split(' '))))

# 가능한 경우의 수 : 상 하 좌 우
q = deque()
q.append((B, 0))

answer = 0
while q:
    temp_B, count = q.popleft()
    if count == 5:
        continue

    # 상
    up_B = [[0] * N for _ in range(N)]
    for i in range(N):  # 열
        visited = False
        col_B = [l[i] for l in temp_B]
        cursor = 1
        while cursor < len(col_B):  # 행
            if col_B[cursor] != 0 and col_B[cursor] == col_B[cursor - 1] and not visited:
                visited = True
                col_B[cursor] *= 2
                col_B.pop(cursor - 1)
                col_B.append(0)
            else:
                visited = False
                cursor += 1
        for j in range(N):
            up_B[j][i] = col_B[j]
    if temp_B != up_B:
        q.append((up_B, count + 1))
    # 하

    # 좌
    lf_B = [[0] * N for _ in range(N)]
    for i in range(N):  # 행
        visited = False
        row_B = deepcopy(temp_B[i])
        cursor = 1
        while cursor < len(row_B):  # 렬
            if row_B[cursor] != 0 and row_B[cursor] == row_B[cursor - 1] and not visited:
                visited = True
                row_B[cursor] *= 2
                row_B.pop(cursor - 1)
                row_B.append(0)
            else:
                visited = False
                cursor += 1
        for j in range(N):
            lf_B[i][j] = row_B[j]
    if temp_B != lf_B:
        q.append((lf_B, count + 1))

    # 우
    rt_B = [[0] * N for _ in range(N)]
    for i in range(N):  # 행
        visited = False
        row_B = deepcopy(temp_B[i])
        for j in range(N-2, -1, -1):  # 렬
            if row_B[j + 1] == 0:
                visited = False
                c = j
                while c >= 0:
                    if row_B[c] == 0:
                        c -= 1
                    else:
                        row_B[j + 1] = row_B[c]
                        row_B[c] = 0
                        j = c - 1
                        break
            elif row_B[j] == row_B[j + 1] and not visited:
                visited = True
                row_B[j + 1] *= 2
                row_B[j] = 0
            else:
                visited = False
        for j in range(N):
            rt_B[i][j] = row_B[j]
    print(temp_B, rt_B)
    if temp_B != rt_B:
        q.append((rt_B, count + 1))

    for l in temp_B:
        answer = max(answer, max(l))

print(answer)