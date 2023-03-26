import sys
input = sys.stdin.readline
MOD = 1000000007


def pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base

    split = pow(base, exp // 2)
    if exp % 2 == 0:
        return split * split % MOD
    else:
        return split * split * base % MOD


N = int(input())
M = sorted(map(int, input().split()))

answer = 0
for i in range(N):
    answer += (M[i] * pow(2, i))
    answer -= (M[i] * pow(2, N - 1 - i))
print(answer % MOD)
