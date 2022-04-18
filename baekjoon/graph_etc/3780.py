import sys
input = sys.stdin.readline



for _ in range(int(input())):
    N = int(input())
    while True:
        data = input().split()
        op = data[0]

        if op == 'O':
            break
        elif op == 'E':
            pass
        elif op == 'I':
            pass