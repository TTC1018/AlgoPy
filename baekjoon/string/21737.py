import sys
input = sys.stdin.readline


def eval(a, sign, b):
    result = 0
    if sign == 'S':
        result = a - b
    elif sign == 'M':
        result = a * b
    elif sign == 'U':
        result = a // b if a > 0 else -(abs(a)//b)
    elif sign == 'P':
        result = a + b
    return str(result)


N = int(input())
S = input().rstrip()

prv, nxt = [], []
answer = []
sign = ''
for c in S:
    if c.isdigit():
        if sign:
            nxt.append(c)
        else:
            prv.append(c)
    else:
        if sign and sign != 'C':
            prv = [eval(int(''.join(prv)), sign, int(''.join(nxt)))]
            nxt.clear()

        if c == 'C':
            answer.append(int(''.join(prv)))
        sign = c

if answer:
    print(*answer)
else:
    print('NO OUTPUT')