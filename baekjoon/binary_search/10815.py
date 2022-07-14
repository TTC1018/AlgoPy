import sys
input = sys.stdin.readline


N = int(input())
C = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

C.sort()
for t in T:
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2

        if C[mid] < t:
            start = mid + 1
        elif C[mid] > t:
            end = mid - 1
        else:
            print(1, end=' ')
            break
    else:
        print(0, end=' ')
