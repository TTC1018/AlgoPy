import sys
input = sys.stdin.readline


def isPal(left, right, dFlag, s):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if not dFlag and (isPal(left + 1, right, True, s) == 0 or isPal(left, right - 1, True, s) == 0):
                return 1
            else:
                return 2
    return 0

answer = []
for _ in range(int(input())):
    s = input().rstrip()
    answer.append(isPal(0, len(s) - 1, False, s))

print('\n'.join(map(str, answer)))
