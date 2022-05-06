in_range = lambda x, y: 0 <= x < R and 0 <= y < C
import sys
input = sys.stdin.readline


def sum_dust():
    global A
    
    result = 0
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                result += A[i][j]
    return result


def spread():
    global A
    
    result = [[0] * C for _ in range(R)]
    ac_up, ac_down = AC
    ux, uy = ac_up
    dx, dy = ac_down
    result[ux][uy], result[dx][dy] = -1, -1
    
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                dust = A[i][j]
                for d in direc:
                    ni, nj = i + d[0], j + d[1]
                    if in_range(ni, nj):
                        if A[ni][nj] != -1:
                            result[ni][nj] += (A[i][j] // 5)
                            dust -= (A[i][j] // 5)
                result[i][j] += dust
    
    A = result


def air_conditioning():
    global A
    
    ac_up, ac_down = AC
    ux, uy = ac_up
    dx, dy = ac_down
    
    result = [[0] * C for _ in range(R)]
    result[ux][uy], result[dx][dy] = -1, -1
    
    uy, dy = uy + 1, dy + 1 # 우측 한칸 옆 부터 시작
    #위 반시계 순환
    while uy != C - 1:
        if A[ux][uy] > 0:
            result[ux][uy + 1] = A[ux][uy]
        uy += 1
    while ux != 0:
        if A[ux][uy] > 0:
            result[ux - 1][uy] = A[ux][uy]
        ux -= 1
    while uy != 0:
        if A[ux][uy] > 0:
            result[ux][uy - 1] = A[ux][uy]
        uy -= 1
    while ux != ac_up[0] - 1:
        if A[ux][uy] > 0:
            result[ux + 1][uy] = A[ux][uy]
        ux += 1
    
    #아래 시계 순환
    while dy != C - 1:
        if A[dx][dy] > 0:
            result[dx][dy + 1] = A[dx][dy]
        dy += 1
    while dx != R - 1:
        if A[dx][dy] > 0:
            result[dx + 1][dy] = A[dx][dy]
        dx += 1
    while dy != 0:
        if A[dx][dy] > 0:
            result[dx][dy - 1] = A[dx][dy]
        dy -= 1
    while dx != ac_down[0] + 1:
        if A[dx][dy] > 0:
            result[dx - 1][dy] = A[dx][dy]
        dx -= 1
    
    for i in range(1, ac_up[0]):
        for j in range(1, C - 1):
            result[i][j] = A[i][j]
    for i in range(ac_down[0] + 1, R - 1):
        for j in range(1, C - 1):
            result[i][j] = A[i][j]
    
    A = result

direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
AC = [0, 0]
for i in range(R):
    if A[i][0] == -1:
        AC = [(i, 0), (i + 1, 0)]
        break

for i in range(T):
    spread()
    air_conditioning()
print(sum_dust())