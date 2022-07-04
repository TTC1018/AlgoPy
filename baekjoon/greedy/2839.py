import sys
input = sys.stdin.readline


N = int(input())

div, mod = divmod(N, 5)
if not mod % 3:
    print(div + mod // 3)
else:
    while div > 0:
        div -= 1
        mod += 5
        if not mod % 3:
            print(div + mod // 3)
            sys.exit()
    print(-1)
