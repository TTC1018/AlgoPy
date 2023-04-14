import sys
input = sys.stdin.readline

# CCW 알고리즘
def ccw(p1, p2, p3):
    p1x, p1y = p1
    p2x, p2y = p2
    p3x, p3y = p3

    return (p1x * p2y + p2x * p3y + p3x * p1y) - (p1y * p2x + p2y * p3x + p3y * p1x)

# p1x p2x p3x
# p1y p2y p3y

P = [tuple(map(int, input().split())) for _ in range(3)]
calc = ccw(P[0], P[1], P[2])
if calc > 0: # 시계 방향
    print(1)
elif calc < 0: # 반시계 방향
    print(-1)
else: # 일직선
    print(0)