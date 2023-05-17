from math import floor
import sys
input = sys.stdin.readline


X, Y = map(int, input().split())
target = floor(Y * 100 / X)
if target >= 99:
    print(-1)
    exit()

left, right = 0, 1000000000
answer = 0
while left <= right:
    mid = (left + right) // 2
    new_percen = floor((Y + mid) * 100 / (X + mid))

    if new_percen > target:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)
