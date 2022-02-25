def check_complete(strs):
    left = 0
    for s in strs:
        if s == '(':
            left += 1
        else:
            if left <= 0:
                return False
            left -= 1
    return True


def find_balance(strs):
    left = 0
    for i in range(len(strs)):
        if strs[i] == '(':
            left += 1
        else:
            left -= 1

        if left == 0:
            return i


def solution(p):
    answer = ''
    if p == '':
        return answer

    split = find_balance(p)
    u, v = p[:split + 1], p[split + 1:]

    if check_complete(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)

    return answer


solution(')(')