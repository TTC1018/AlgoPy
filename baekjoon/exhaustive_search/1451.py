args = input().split(' ')
N = int(args[0]) # 세로 1..100
M = int(args[1]) # 가로 1..100

answer = 1
nums = []
for i in range(0, N):
    nums.append([int(''.join(n)) for n in input()])


