def transform(num, k):
    result = ''
    while num > 0:
        num, mod = divmod(num, k)
        result += str(mod)
    
    return result[::-1]


# 에라토스테네스의 체로는 못 품 (메모리 초과)
def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**(1/2)) + 1):
            if num % i == 0:
                return False
        return True


def solution(n, k):
    answer = 0
    n = transform(n, k)
    n = n.split('0')

    for cand in n:
        if len(cand) > 0:
            if isPrime(int(cand)):
                answer += 1

    return answer