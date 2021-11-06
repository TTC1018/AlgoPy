N = int(input())
nums = []
for i in range(N):
    nums.append(input())


def solve():
    for n in nums:
        i = len(n)
        for alpha in n:
            vals[ord(alpha) - 65] += 10**(i - 1)
            i -= 1

    vals.sort(reverse=True)
    result = 0
    for i in range(9):
        result += vals[i] * (9 - i)
    return result


vals = [0] * 26
print(solve())
print(vals)