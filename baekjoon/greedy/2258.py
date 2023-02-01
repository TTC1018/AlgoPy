import sys
input = sys.stdin.readline


N, M = map(int, input().split())
meats = [tuple(map(int, input().split())) for _ in range(N)]
meats.sort(key=lambda x: (x[1], -x[0]))

prefix = [[0, 0] for _ in range(N)]
prefix[0] = [meats[0][0], meats[0][1]]

for i in range(1, N):
    prefix[i][0] = meats[i][0] + prefix[i - 1][0]
    if meats[i][1] == meats[i - 1][1]:
        prefix[i][1] = meats[i][1] + prefix[i - 1][1]
    else:
        prefix[i][1] = meats[i][1]
prefix.sort(key=lambda x: (x[1], -x[0]))

for i in range(N):
    if prefix[i][0] >= M:
        print(prefix[i][1])
        break
else:
    print(-1)