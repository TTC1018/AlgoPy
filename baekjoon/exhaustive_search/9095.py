# 다이나믹 프로그래밍??

# 1 : 1 => dp[1]
# 2 : 1+1, 2 => dp[2]
# 3 : 1+2, 1+1+1, 2+1, 3
# 4 : 1+3, 1+1+2, 2+2, 1+2+1, 1+1+1+1, 2+1+1, 3+1 => dp[1] + dp[2] + dp[3]

T = int(input())
nums = []
for i in range(T):
    nums.append(int(input()))

max_num = max(nums)
dp = []

dp += [1, 2, 4]

if(max_num >= 4):
    for i in range(3, max_num):
        dp.insert(i, dp[i-1] + dp[i-2] + dp[i-3])

for num in nums:
    print(dp[num-1])
