import sys
input = sys.stdin.readline

def count_of_two(num):
    cnt = 0
    while num > 0:
        num //= 2 # 2^n이 몇개인지 구하기 (2의 배수, 4의 배수, 8의 배수...)
        cnt += num
    return cnt

def count_of_five(num):
    cnt = 0
    while num > 0:
        num //= 5 # 5^n이 몇개인지 구하기 (5의 배수, 25의 배수, ...)
        cnt += num
    return cnt


# 0의 개수 = 10이 나올 때마다 늘어남
n, m = map(int, input().split())
a1 = count_of_two(n) - count_of_two(n - m) - count_of_two(m)
a2 = count_of_five(n) - count_of_five(n - m) - count_of_five(m)
print(min(a1, a2))