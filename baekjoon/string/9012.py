import sys
input = sys.stdin.readline


for _ in range(int(input())):
    S = input().rstrip()

    stack = []

    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')