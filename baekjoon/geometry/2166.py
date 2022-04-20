# 외적 구하는 식
def calc_ex(sp, p1, p2):
    # ABC = (0.5)*AB*AC
    result = (p1[0] - sp[0])*(p2[1] - sp[1]) - (p1[1] - sp[1])*(p2[0] - sp[0])
    return result / 2 # 삼각형은 평행사변형의 1/2


def calc_area():
    area = 0
    sp = P[0]
    for i in range(1, N - 1):
        area += calc_ex(sp, P[i], P[i + 1])
    return area


N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))
print('{0:.1f}'.format(abs(calc_area())))