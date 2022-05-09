from collections import deque
import sys


def spin(wheel, direc):
    if direc == 1: # 시계
        wheels[wheel].appendleft(wheels[wheel].pop())
    elif direc == -1: # 반시계
        wheels[wheel].append(wheels[wheel].popleft())


def go(wheel, direc):
    if not visited[wheel]: # 이미 회전한 톱니는 중복 회전 되지 않도록
        visited[wheel] = True
        
        if wheel == 1:
            if wheels[1][2] != wheels[2][6]:
                go(2, -direc)
        elif wheel == 4:
            if wheels[3][2] != wheels[4][6]:
                go(3, -direc)
        else:
            if wheels[wheel][6] != wheels[wheel - 1][2] and wheels[wheel][2] != wheels[wheel + 1][6]:
                go(wheel - 1, -direc)
                go(wheel + 1, -direc)
            elif wheels[wheel][6] != wheels[wheel - 1][2]:
                go(wheel - 1, -direc)
            elif wheels[wheel][2] != wheels[wheel + 1][6]:
                go(wheel + 1, -direc)
        spin(wheel, direc)


wheel_1 = deque(list(map(int, list(sys.stdin.readline().rstrip()))))
wheel_2 = deque(list(map(int, list(sys.stdin.readline().rstrip()))))
wheel_3 = deque(list(map(int, list(sys.stdin.readline().rstrip()))))
wheel_4 = deque(list(map(int, list(sys.stdin.readline().rstrip()))))
wheels = [-1, wheel_1, wheel_2, wheel_3, wheel_4]

for _ in range(int(sys.stdin.readline().rstrip())):
    W, D = map(int, sys.stdin.readline().rstrip().split())
    # 옆 톱니와 맞닿는 위치 = 우측 2, 좌측 6 인덱스
    visited = [False] * 5
    go(W, D)

answer = wheels[1][0] + 2*wheels[2][0] + 4*wheels[3][0] + 8*wheels[4][0]
print(answer)