from heapq import heappush, heappop

n = int(input())
uni = [tuple(map(int, input().split())) for _ in range(n)]
uni.sort(key=lambda x: x[1])

q = []
for u in uni:
    heappush(q, u[0])
    if len(q) > u[1]: # 제한 일자보다 많은 요소가 담겨져 있으면
        heappop(q) # 강연료 적은 것 삭제
print(sum(q))