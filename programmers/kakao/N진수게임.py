mods = ['A', 'B', 'C', 'D', 'E', 'F']
def returning_n(num, n):
    result = ''

    while num > 0:
        num, mod = divmod(num, n)
        if mod >= 10:
            result += mods[mod - 10]
        else:
            result += str(mod)

    return result[::-1]



def solution(n, t, m, p):
    limit = t*m
    arr = ['0']

    for i in range(1, limit):
        arr += list(returning_n(i, n))

    return ''.join(arr[p - 1:p - 1 + t*m:m])


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))