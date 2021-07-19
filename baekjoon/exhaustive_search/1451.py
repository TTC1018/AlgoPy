# 직사각형으로 3등분 하기

def getSum(nums, sx, sy, ex, ey):
    sum = 0
    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            sum += nums[i][j]
    return sum

args = input().split(' ')
N = int(args[0]) # 세로 1..100
M = int(args[1]) # 가로 1..100

answer = 0
nums = []
for i in range(N):
    nums.append([int(''.join(n)) for n in input()])

# 세로 3등분
for i in range(N-2):
    for j in range(i+1, N-1):
        sq1 = getSum(nums, 0, 0, i, M-1)
        sq2 = getSum(nums, i+1, 0, j, M-1)
        sq3 = getSum(nums, j+1, 0, N-1, M-1)
        answer = max(answer, sq1*sq2*sq3)

# 가로 3등분
for i in range(M-2):
    for j in range(i+1, M-1):
        sq1 = getSum(nums, 0, 0, N-1, i)
        sq2 = getSum(nums, 0, i+1, N-1, j)
        sq3 = getSum(nums, 0, j+1, N-1, M-1)
        answer = max(answer, sq1*sq2*sq3)

for i in range(M-1, 0, -1):
    for j in range(N-1):
        sq1 = getSum(nums, 0, i, N-1, M-1)
        sq2 = getSum(nums, 0, 0, j, i-1)
        sq3 = getSum(nums, j+1, 0, N-1, i-1)
        answer = max(answer,sq1*sq2*sq3)

for i in range(M-1):
    for j in range(N-1):
        sq1 = getSum(nums, 0, 0, N-1, i)
        sq2 = getSum(nums, 0, i+1, j, M-1)
        sq3 = getSum(nums, j+1, i+1, N-1, M-1)
        answer = max(answer,sq1*sq2*sq3)

for i in range(N-1):
    for j in range(M-1):
        sq1 = getSum(nums, 0, 0, i, M-1)
        sq2 = getSum(nums, i+1, 0, N-1, j)
        sq3 = getSum(nums, i+1, j+1, N-1, M-1)
        answer = max(answer,sq1*sq2*sq3)

for i in range(N-1, 0, -1):
    for j in range(M-1):
        sq1 = getSum(nums, i, 0, N-1, M-1)
        sq2 = getSum(nums, 0, 0, i-1, j)
        sq3 = getSum(nums, 0, j+1, i-1, M-1)
        answer = max(answer,sq1*sq2*sq3)

print(answer)