from collections import deque
import sys
input = sys.stdin.readline


def calc(n1, sign, n2):
    if sign == '+':
        return n1 + n2
    elif sign == '*':
        return n1 * n2
    elif sign == '-':
        return n1 - n2
    else:
        if n1*n2 < 0 and n1%n2 != 0:
            return (n1 // n2) + 1
        return n1 // n2

S = input().rstrip()
q = deque()
num = None
neg = False
for s in S:
    if s.isdigit():
        if num == None:
            num = 0
        num *= 10
        num += int(s)
    else:
        if num == None:
            neg = True
        else:
            if neg:
                q.append(-num)
                neg = False
            else:
                q.append(num)
            q.append(s)
            num = None

if neg:
    q.append(-num)
    neg = False
else:
    q.append(num)

pd, pm = {'*', '/'}, {'+', '-'}
while len(q) > 1:
    result = 'front'
    op1 = q[1]
    op2 = q[-2]

    if op1 in pm and op2 in pd:
        result = 'back'
    elif op1 in pd and op2 in pm:
        result = 'front'
    else:
        left = calc(q[0], q[1], q[2])
        right = calc(q[-3], q[-2], q[-1])
        if left > right:
            result = 'front'
        elif left < right:
            result = 'back'
        else:
            result = 'front'

    if result == 'front':
        calc_result = calc(q[0], q[1], q[2])
        for _ in range(3):
            q.popleft()
        q.appendleft(calc_result)
    else:
        calc_result = calc(q[-3], q[-2], q[-1])
        for _ in range(3):
            q.pop()
        q.append(calc_result)

print(q[0])