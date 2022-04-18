X, Y, W, S = map(int, input().split())
# (0, 0) -> (X, Y)
bigger, smaller = max(X, Y), min(X, Y)

case1 = W*X + W*Y
odd_check = (X + Y) % 2
case2 = (bigger - odd_check) * S + odd_check * W
case3 = smaller * S + (bigger - smaller) * W

print(min(case1, case2, case3))
# 다 직선으로 가기 (2W < S)
# 다 대각선 or 거의 다 대각선 + 직선 1개 (2S < 2W)
# 짧은 쪽에 대각선 쓰다가 남은 거 직선 (S < 2W < 2S)