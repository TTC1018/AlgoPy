def prime(num):
    if num < 2:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


T = int(input())
for i in range(T):
    A, B = [int(''.join(n)) for n in input().split(' ')]
    answer = 0
