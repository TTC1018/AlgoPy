

n = int(input())
m = int(input())
nums = [int(('').join(n)) for n in input().split(' ')]

if(n==100):
    print(0)
    exit()

start = 100

num_split = [int(('').join(num)) for num in list(str(n))]
num_split = list(set(num_split))

if set(nums).issubset(set(num_split)):
    print("YES")

