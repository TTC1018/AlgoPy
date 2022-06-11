from collections import deque
import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    l = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if not n:
        l = deque()

    r_flag = False
    for op in p:
        if op == 'D':

            if n:
                if r_flag:
                    l.pop()
                else:
                    l.popleft()
                n -= 1
            else:
                print('error')
                break
        elif op == 'R':
            r_flag = not r_flag
    else:
        if r_flag:
            l.reverse()
        print('[' + ','.join(l) + ']')