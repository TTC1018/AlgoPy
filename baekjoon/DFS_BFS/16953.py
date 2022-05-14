from collections import deque
import sys
input = sys.stdin.readline


A, B = map(int, input().split())
q = deque()
q.append((A, 0))

while q:
    now, cnt = q.popleft()

    if now == B:
        print(cnt + 1)
        sys.exit()

    if now > B:
        continue

    q.append((now * 2, cnt + 1))
    q.append((int(str(now) + '1'), cnt + 1))
print(-1)