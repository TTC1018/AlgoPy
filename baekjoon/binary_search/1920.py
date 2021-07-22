N = int(input())
A = [int(''.join(n)) for n in input().split(' ')]
M = int(input())
nums = [int(''.join(n)) for n in input().split(' ')]

A = sorted(A)
answer = 0
for n in nums:
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if n == A[mid]:
            answer = 1
            break
        elif n < A[mid]:
            right = mid - 1
            answer = 0
        elif n > A[mid]:
            left = mid + 1
            answer = 0
    print(answer)