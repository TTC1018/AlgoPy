from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
cup = [tuple(map(int, input().split())) for _ in range(N)]
cup.sort(key=lambda x: x[0])

q = []
for i in range(N):
    heappush(q, cup[i][1]) # 일단 리스트에 삽입
    if len(q) > cup[i][0]: # 데드라인보다 요소가 많이 들어있을 때 (자리가 없을 때)
        heappop(q) # 컵라면 수 가장 작은 요소 제거
print(sum(q))