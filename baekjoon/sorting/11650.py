N = int(input())

nums = []
for i in range(N):
    nums.append(tuple(map(int, input().split())))

nums.sort(key=lambda x:(x[0], x[1]))

for n in nums:
    print(n[0], n[1])