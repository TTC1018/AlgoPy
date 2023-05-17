import sys
input = sys.stdin.readline

n = int(input())
N = sorted(map(int, input().split()))
x = int(input())

answer = 0
for i in range(n):
    target = x - N[i]
    if target > 0 and target != N[i]:
        left, right = i + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == N[mid]:
                answer += 1
                break
            elif target > N[mid]:
                left = mid + 1
            elif target < N[mid]:
                right = mid - 1
print(answer)