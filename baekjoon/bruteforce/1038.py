import sys
input = sys.stdin.readline


N = int(input())
num = [str(i) for i in range(10)]

answer = num[:]
added = num[:]
while added:
    nxt = []
    for i in range(1, 10):
        for n in added:
            if i > int(n[0]):
                nxt.append(str(i) + n)
    answer.extend(nxt)
    added = nxt

if len(answer) <= N:
    print(-1)
else:
    print(answer[N])