import sys
input = sys.stdin.readline


while True:
    S = input().rstrip()
    if S == '.':
        break

    stack = []
    for s in S:
        if s == '(':
            stack.append('(')
        elif s == '[':
            stack.append('[')
        elif s == ')':
            if stack and stack[-1] == '(':
                    stack.pop()
            else:
                print('no')
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')

