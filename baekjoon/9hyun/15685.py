import sys
input = sys.stdin.readline
in_range = lambda x, y: 0 <= x <=100 and 0 <= y <= 100


def make_d_curve(y, x, d, g):
    covered[x][y] = True
    
    dc = [d]
    for _ in range(g):
        for i in range(len(dc) - 1, -1, -1): # 이전 세대 커브 역순으로 90도 회전 방향을 가짐
            dc.append((dc[i] + 1) % 4)
    
    for i in range(len(dc)):
        x, y = x + direc[dc[i]][0], y + direc[dc[i]][1]
        if in_range(x, y):
            covered[x][y] = True
    

N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]

direc = [(0, 1), (-1, 0), (0, -1), (1, 0)]
covered = [[False] * 101 for _ in range(101)]

for y, x, d, g in curves:
    make_d_curve(y, x, d, g)

answer = 0
for i in range(100):
    for j in range(100):
        if covered[i][j] and covered[i + 1][j] and covered[i][j + 1] and covered[i + 1][j + 1]:
            answer += 1
print(answer)