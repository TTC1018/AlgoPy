from collections import deque
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    x, y = map(int, input().split())
    c = [tuple(map(int, input().split())) for _ in range(n)]
    dx, dy = map(int, input().split())
    visited = [False] * n

    q = deque([(x, y)])
    while q:
        nx, ny = q.popleft()
        if abs(nx - dx) + abs(ny - dy) <= 1000:
            print('happy')
            break

        for i in range(n):
            if not visited[i]:
                bx, by = c[i]
                dist = abs(nx - bx) + abs(ny - by)
                if dist <= 1000:
                    visited[i] = True
                    q.append((bx, by))
    else:
        print('sad')
