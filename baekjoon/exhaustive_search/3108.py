N = int(input())

visited = [[False] * 1001] * 1001

PU = 0

visited[500][500] = True
for i in range(N):
    PU_flag = True
    x1, y1, x2, y2 = list(map(int, input().split(' ')))
    for x_range in range(x1 + 500, x2 + 500 + 1):
        if visited[x_range][y1] or visited[x_range][y2]:
            PU_flag = False
            print('changed in ({},y)'.format(x_range))
            break

    if PU_flag:
        for y_range in range(y1 + 500, y2 + 500 + 1):
            if visited[x1][y_range] or visited[x2][y_range]:
                PU_flag = False
                print('changed in (x,{})'.format(y_range))
                break

    if PU_flag:
        PU += 1

    for x_range in range(x1 + 500, x2 + 500 + 1):
        visited[x_range][y1] = True
        visited[x_range][y2] = True
    for y_range in range(y1 + 500, y2 + 500 + 1):
        visited[x1][y_range] = True
        visited[x2][y_range] = True


print(PU)
