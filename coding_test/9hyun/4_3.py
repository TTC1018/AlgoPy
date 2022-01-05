N, M = map(int, input().split(' '))
x, y, d = map(int, input().split(' '))

m = []
check = [[0] * M for i in range(N)]

direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(N):
    m.append(list(map(int, input().split(' '))))
    for j in range(M):
        if m[i][j] == 1:
            check[i][j] = 1

answer, turned = 0, 0
while True:
    d = d - 1 if d - 1 >= 0 else 3 # 일단 왼쪽으로 돌고 난 뒤의 상황에 초점을 맞추기

    nx = x + direc[d][0]
    ny = y + direc[d][1]

    if check[nx][ny] == 0:
        check[nx][ny] = 1
        x, y = nx, ny
        answer += 1
        turned = 0
        continue
    else:
        turned += 1 # 회전만

    if turned == 4: # 계속 회전 중일 때 (사방이 막힘)
        nx = x - direc[d][0]
        ny = y - direc[d][1]
        if m[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turned = 0

print(answer)



