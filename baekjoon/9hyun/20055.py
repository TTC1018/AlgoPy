from collections import deque
import sys
input = sys.stdin.readline


def belt_exec():
    A.appendleft(A.pop())
    R.appendleft(R.pop())


def robot_move():
    # 내릴 로봇 있는지
    if R[off_loc]:
        R[off_loc] = False

    if R[off_loc - 1] and A[off_loc] > 0:
        R[off_loc - 1] = False
        A[off_loc] -= 1

    # 로봇들 다음 칸으로 보내기
    for i in range(N - 3, -1, -1):
        if R[i] and not R[i + 1] and A[i + 1] > 0:
            R[i], R[i + 1] = False, True
            A[i + 1] -= 1


N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
R = deque([False for _ in range(2*N)])
put_loc, off_loc = 0, N - 1

step = 1
while True:
    # 벨트 회전
    belt_exec()

    # 로봇 이동
    robot_move()

    # 로봇 올리기
    if A[put_loc] > 0:
        R[put_loc] = True
        A[put_loc] -= 1

    # 내구도 확인
    if A.count(0) >= K:
        break
    step += 1
print(step)