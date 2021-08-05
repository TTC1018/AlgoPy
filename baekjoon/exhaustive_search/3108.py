def solve(y, x):
    points[y][x] = 2

    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_y = y + i
        new_x = x + j
        if 0 <= new_y <= 2000 and 0 <= new_x <= 2000:
            if points[new_y][new_x] == 1:
                solve(new_y, new_x)


N = int(input())

points = []
for i in range(2001):
    points.append([0] * 2001)

starts = []
for i in range(N):
    nums = list(map(int, input().split(' ')))
    x1, y1, x2, y2 = list(map(lambda n: (n + 500) * 2, nums))
    starts.append((x1, y1))

    for x_range in range(x1, x2 + 1):
        points[y1][x_range] = 1
        points[y2][x_range] = 1
    for y_range in range(y1, y2 + 1):
        points[y_range][x1] = 1
        points[y_range][x2] = 1

PU = 0
for sx, sy in starts:
    if points[sy][sx] == 1:
        solve(sy, sx)
        PU += 1
PU = PU - 1 if points[1000][1000] == 2 else PU
print(PU)
