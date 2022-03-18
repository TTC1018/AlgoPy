import sys
from collections import deque
def reverse(strs):
    result = ''
    for s in strs:
        if s == '0':
            result += '1'
        else:
            result += '0'
    return result

N = int(input())
origin, target = input(), input()

visited = [origin]
next = deque()
next.append((origin, 0))

answer = sys.maxsize
while next:
    now, count = next.popleft()

    cand = ''
    for i in range(N):
        if i == 0:
            cand = reverse(now[:2]) + now[2:]
        elif i == N - 1:
            cand = now[:N - 1] + reverse(now[N - 1:])
        else:
            cand = now[:i - 1] + reverse(now[i - 1:i + 2]) + now[i + 2:]

        if not (cand in visited):
            visited.append(cand)
            if cand == target:
                answer = min(answer, count + 1)
            else:
                next.append((cand, count + 1))

if answer != sys.maxsize:
    print(answer)
else:
    print(-1)