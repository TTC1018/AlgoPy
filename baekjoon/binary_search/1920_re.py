N = int(input())
A = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

A.sort()
for t in T:
    start, end = 0, N - 1
    flag = 0
    while start <= end:
        mid = (start + end) // 2

        if t < A[mid]:
            end = mid - 1
        elif t > A[mid]:
            start = mid + 1
        else:
            flag = 1
            break
    print(flag)