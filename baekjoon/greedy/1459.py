X, Y, W, S = map(int, input().split())

bigger, smaller = max(X, Y), min(X, Y)
isOdd = (X + Y) % 2

a1 = (X + Y) * W # 평행 이동만
a2 = smaller * S + (bigger - smaller) * W # 대각선 + 평행이동
a3 = (bigger - isOdd) * S + isOdd * W # 대각선 최대한 많이 사용하는 경우
answer = min(a1, a2, a3)

print(answer)