import sys
input = sys.stdin.readline

N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]
tasks.sort(key=lambda x:-x[1]) # 데드라인 내림차순 정렬

start = tasks[0][1]
for t, s in tasks:
    start = min(s, start)
    if start < 0:
        print(-1)
        break
    start -= t
else:
    if start >= 0:
        print(start)
    else:
        print(-1)