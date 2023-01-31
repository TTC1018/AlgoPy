import sys
input = sys.stdin.readline

N = int(input())
A = list(sorted(map(int, input().split())))

answer = 0
for i in range(N):
    left, right = 0, N - 1
    while left < right:
        sum_val = A[left] + A[right]
        if sum_val == A[i]:
            if i == left:
                left += 1
            elif i == right:
                right -= 1
            else:
                answer += 1
                break
        elif sum_val < A[i]:
            left += 1
        elif sum_val > A[i]:
            right -= 1
print(answer)
