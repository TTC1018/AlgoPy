INF = 1e9

X, Y, W, S = map(int, input().split())

bigger, smaller = max(X, Y), min(X, Y)

answer = 0
if 2 * W > S:
    answer = (bigger // 2) * 2 * S + (bigger % 2) * W
else:
    answer = (X + Y) * W
print(answer)