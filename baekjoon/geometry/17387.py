import sys
input = sys.stdin.readline

def ccw(p1, p2, p3): # 외적을 이용한 풀이
    # 점 A, B, C가 있다고 했을 때
    # 벡터AB * 벡터 BC = 양수:반시계 / 0:직선 / 음수:시계 방향임을 알 수 있음
    # 벡터AB = 좌표B - 좌표A / 벡터bc = 좌표C - 좌표B
    # (Bx - Ax, By - Ay) / (Cx - Bx, Cy - By) (2차원 좌표라 3차원 좌표값 다 0임. 없다고 생각해도 됨)
    # 외적 : (Bx - Ax)(Cy - By) - (By - Ay)(Cx - Bx)
    op = (p2[0] - p1[0])*(p3[1] - p2[1]) - (p2[1] - p1[1])*(p3[0] - p2[0])
    if op > 0:
        return 1
    elif op == 0:
        return 0
    else:
        return -1


p1p2 = list(map(int, input().split()))
p1, p2 = tuple(p1p2[:2]), tuple(p1p2[2:])
p3p4 = list(map(int, input().split()))
p3, p4 = tuple(p3p4[:2]), tuple(p3p4[2:])

check1 = ccw(p1, p2, p3) * ccw(p1, p2, p4) # 하나는 반시계, 다른 하나는 시계면 곱했을 때 음수가 나옴
check2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if check1 == 0 and check2 == 0: # 평행인데 겹치는 경우 판단
    if p1 > p2: # 더 큰 좌표를 뒷점으로 설정
        p1, p2 = p2, p1
    if p3 > p4:
        p3, p4 = p4, p3
    if p1 <= p4 and p3 <= p2: # 서로 겹치면
        print(1)
    else:
        print(0)
else:
    if check1 <= 0 and check2 <= 0:
        print(1)
    else:
        print(0)