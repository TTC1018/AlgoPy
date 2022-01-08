
N = int(input())
items = list(map(int, input().split()))

M = int(input())
c_list = list(map(int, input().split()))

for target in c_list:
    start, end = 0, len(items) - 1
    result = False
    while start <= end:
        mid = (start + end) // 2

        if items[mid] == target:
            result = True
            break
        elif items[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    if result == True:
        print('yes')
    else:
        print('no')