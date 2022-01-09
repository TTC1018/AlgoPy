import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 1, max(trees)

answer = 0
while start <= end:
    mid = (start + end) // 2

    t_sum = sum([t - mid if t > mid else 0 for t in trees]) # 리스트 내포가 for문보다 성능 좋음

    if t_sum < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)