import sys
input = sys.stdin.readline

R, C = map(int, input().split())
word = [input().rstrip() for _ in range(R)]

cnt = 0
start, end = 0, R - 1
while start <= end:
    mid = (start + end) // 2

    s = set()
    for j in range(C):
        tmp = ''
        for i in range(mid, R):
            tmp += word[i][j]

        if tmp in s:
            end = mid - 1
            break
        s.add(tmp)
    else:
        cnt = mid
        start = mid + 1
print(cnt)