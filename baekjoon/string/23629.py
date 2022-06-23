import sys
sys.setrecursionlimit(10 ** 5)


def madness_check(r):
    if not r:
        print('Madness!')
        sys.exit()


def calc(stk, l, r):
    sign = stk.pop().replace('x', '*')
    return int(eval(l + sign + r))


M = input().rstrip()
m_len = len(M)
for i in range(m_len - 1):
    if not M[i].isalpha() and not M[i + 1].isalpha():
        print('Madness!')
        sys.exit()

d = {'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4', 'FIVE': '5',
     'SIX': '6', 'SEVEN': '7', 'EIGHT': '8', 'NINE': '9', 'ZERO': '0'}
for alpha in d:
    M = M.replace(alpha, str(d[alpha]))

answer = 0
left, right = '', ''
stack = []
for m in M:
    if m.isnumeric():
        if stack:
            right += m
        else:
            left += m
    else:
        if m == '=':
            if stack:
                madness_check(right)
                answer = calc(stack, left, right)
                left, right = '', ''
            else:
                answer += eval(left)
                left = ''
        else:
            if stack:
                madness_check(right)
                answer = calc(stack, left, right)
                left, right = str(answer), ''
            stack.append(m)

print(M)
answer = str(answer)
for alpha in d:
    answer = answer.replace(d[alpha], alpha)
print(answer)
