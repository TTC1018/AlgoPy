def solve(num):
    digits = list(map(int, num))
    length = len(digits)

    if length <= 2:
        return True
    else:
        val = digits[1] - digits[0]
        for i in range(length - 1):
            if digits[i + 1] - digits[i] != val:
                return False
        return True

target = input()
answer = 0

for i in range(1, int(target) + 1):
    if solve(str(i)):
        answer += 1
print(answer)