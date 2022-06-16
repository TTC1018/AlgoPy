import sys
input = sys.stdin.readline


sign = ['+', '-', ' ']
def btk(m, cnt, limit):
    if cnt == limit:
        if not eval(m.replace(' ', '')):
            modi.append(m)
        return

    for s in sign:
        btk(m + s + num[cnt + 1], cnt + 1, limit)


for _ in range(int(input())):
    N = int(input())
    num = [str(n) for n in range(1, N + 1)]
    modi = []
    btk(num[0], 0, N - 1)
    modi.sort()

    for m in modi:
        print(m)
    print()
