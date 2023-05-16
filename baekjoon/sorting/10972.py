import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    if nums[i - 1] < nums[i]:
        for j in range(N - 1, i - 1, -1):
            if nums[i - 1] < nums[j]:
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break
        nums = nums[:i] + sorted(nums[i:])
        print(*nums)
        break
else:
    print(-1)