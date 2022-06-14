import sys
input = sys.stdin.readline

s = input().rstrip()
if s in ['P', 'PPAP']:
    print('PPAP')
    sys.exit()

s_len = len(s)
check = list('PPAP')

stack = []
for alpha in s:
    stack.append(alpha)
    if stack[-4:] == check:
        for _ in range(3):
            stack.pop()

if ''.join(stack) == 'P':
    print('PPAP')
else:
    print('NP')