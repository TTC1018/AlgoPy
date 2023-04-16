import sys
input = sys.stdin.readline


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == N:
        print(num)
    else:
        for digit in range(10):
            temp = int(f'{num}{digit}')
            if is_prime(temp):
                dfs(temp)

N = int(input())
dfs(2)
dfs(3)
dfs(5)
dfs(7)