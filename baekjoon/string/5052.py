import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline().rstrip())
    nums = [sys.stdin.readline().rstrip() for _ in range(n)]
    if n == 1:
        print('YES')
        continue

    nums.sort()
    for i in range(n - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            print('NO')
            break
    else:
        print('YES')