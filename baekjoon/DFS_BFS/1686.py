import sys
from collections import deque
input = sys.stdin.readline
calc_dist = lambda x, y, a, b: ((x-a)**2 + (y-b)**2)**0.5


v, m = map(float, input().split())
xs, ys = map(float, input().split())
xt, yt = map(float, input().split())
bunkers = set()
while True:
    try:
        temp = input()
        if not temp:
            break

        x, y = map(float, temp.split())
        bunkers.add((x, y))
    except:
        break

step_range = v * m * 60
visited = set()
q = deque([(xs, ys, 0)])

while q:
    x, y, cnt = q.popleft()
    if calc_dist(x, y, xt, yt) < step_range:
        print(f'Yes, visiting {cnt} other holes.')
        sys.exit()

    for bunker in bunkers:
        bx, by = bunker
        if bunker not in visited and calc_dist(x, y, bx, by) < step_range:
            visited.add(bunker)
            q.append((bx, by, cnt + 1))

print('No.')