N, x = map(int, input().split())
nums = list(map(int, input().split()))

# 시간 복잡도 O(N)
# answer = nums.count(x)
# if answer == 0:
#     print(-1)
# else:
#     print(answer)


# 시간 복잡도 O(logN)
start, end = 0, N - 1
first = -1
while start <= end: # 맨 앞 x 인덱스 구하기
    mid = (start + end) // 2

    if nums[mid] < x:
        start = mid + 1
    elif nums[mid] == x:
        first = mid
        end = mid - 1
    else:
        end = mid - 1

start, end = 0, N - 1
last = -1
while start <= end: # 맨 뒤 x 인덱스 구하기
    mid = (start + end) // 2

    if nums[mid] < x:
        start = mid + 1
    elif nums[mid] == x:
        last = mid
        start = mid + 1
    else:
        end = mid - 1

answer = last - first + 1
if first != -1:
    print(answer)
else:
    print(-1)