import sys
input = sys.stdin.readline

R, C = map(int, input().split())
word = [input().rstrip() for _ in range(R)]

s = []
for j in range(C):
    tmp = ''
    for i in range(R):
        tmp += word[i][j]
    s.append(tmp)

cnt = 0
while R > 0:
    R -= 1

    nxt = []
    for tmp in s:
        tmp = tmp[1:]
        if tmp in nxt:
            print(cnt)
            sys.exit()
        nxt.append(tmp)

    s = nxt
    cnt += 1