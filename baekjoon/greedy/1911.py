from math import ceil
import sys
input = sys.stdin.readline


N, L = map(int, input().split())
pool = [tuple(map(int, input().split())) for _ in range(N)]
pool.sort(key=lambda x:x[0])

prev = pool[0][0]
cnt = 0
for i in range(N):
    prev = max(prev, pool[i][0]) # 덮은 마지막 지점 vs 다음 웅덩이 시작지점
    if prev < pool[i][1]: # 웅덩이 끝을 못 덮었을 때
        added = ceil((pool[i][1] - prev) / L)
        cnt += added
        prev += (added * L)
print(cnt)