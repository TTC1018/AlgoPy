from copy import deepcopy

n = int(input())
nums = list(map(int, input().split()))
dp = deepcopy(nums)

for i in range(1, n):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])
    # 이어진 연속합 vs 현재값 (연속을 끊기) 중 더 큰 값을 선택
    # 일반적인 dp와 다르게 무조건 연속합을 하는 것을 가정하여 비교함 (마지막에 max 함수로 최대값을 찾아내면 되기 때문)

print(max(dp)) # dp 배열에서 최대값이 해답