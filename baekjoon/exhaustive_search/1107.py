

n = int(input())
m = int(input())
nums = [int(('').join(n)) for n in input().split(' ')]

start = 100

num_split = [int(('').join(num)) for num in list(str(n))]
num_split = set(num_split)

if nums in num_split:
    print("YES")

print(num_split)