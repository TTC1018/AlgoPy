import sys
input = sys.stdin.readline

D, K = map(int, input().split())
fibo = [1, 1]
for _ in range(D - 3):
    fibo.append(fibo[-1] + fibo[-2])

a_d, b_d = fibo[D - 3], fibo[D - 2]
for A in range(1, K // a_d + 1):
    rest = K - (A * a_d)
    if rest % b_d == 0:
        B = rest // b_d
        print(f'{A}\n{B}')
        break
