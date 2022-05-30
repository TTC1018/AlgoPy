from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]
classes.sort(key=lambda x:x[0])


prev = classes[0][1]
cnt = 1
room = [prev]
for i in range(1, N):
    used = heappop(room)
    if used <= classes[i][0]:
        heappush(room, classes[i][1])
    else:
        cnt += 1
        heappush(room, used)
        heappush(room, classes[i][1])
print(cnt)