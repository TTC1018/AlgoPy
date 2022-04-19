import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))

left, right = 0, N - 1
a1, a2 = 0, 0
ideal = sys.maxsize
while left < right:
    temp_sum = T[left] + T[right]

    if abs(temp_sum) < ideal:
        a1, a2 = left, right
        ideal = abs(temp_sum)

    if temp_sum > 0:
        right -= 1
    elif temp_sum < 0:
        left += 1
    else:
        break

print(T[a1], T[a2])