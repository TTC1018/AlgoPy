import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort()
print(round(sum(nums)/N))
print(nums[N // 2])

counts = Counter(nums).most_common()
if N > 1:
    if counts[0][1] == counts[1][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])
else:
    print(counts[0][0])

print(nums[-1] - nums[0])