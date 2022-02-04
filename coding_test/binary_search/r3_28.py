N = int(input())
target = list(map(int, input().split()))

start, end = 0, len(target) - 1
answer = -1
while start <= end:
    mid = (start + end) // 2

    if target[mid] < mid:
        start = mid + 1
    elif target[mid] == mid:
        answer = mid
        break
    else:
        end = mid - 1

print(answer)