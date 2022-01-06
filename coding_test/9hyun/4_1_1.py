import time
stime = time.time()
N = int(input())
routes = input().split(' ')

start = (1, 1)
d = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}


for r in routes:
    n_x = start[0] + d[r][0]
    n_y = start[1] + d[r][1]

    if 1 <= n_x <= 5 and 1 <= n_y <= 5:
        start = (n_x, n_y)
ftime = time.time()

print(start[0], start[1])