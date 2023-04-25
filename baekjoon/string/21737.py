import sys
input = sys.stdin.readline


N = int(input())
S = input().rstrip()

temp = ''
temps = []
sign = ''
signs = {'S', 'M', 'U', 'P'}
answer = []
for s in S:
    if s == 'C':
        if temps:
            answer.append(temps[0])
    elif s in signs:
        if sign:
            temps.append(temps.pop())
            sign = s
        else:
            temps.append(temp)
            sign = s
    elif s.isdigit():
        temp += s

if answer:
    print(*answer)
else:
    print('NO OUTPUT')