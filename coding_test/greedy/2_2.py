N, M, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

nums.sort(reverse=True)

answer = 0
for i in range(M):
    if i % K == 0 and i != 0:
        answer += nums[1]
    else:
        answer += nums[0]

print(answer)