import sys
input = sys.stdin.readline


N = int(input())
L = list(map(int, input().split()))
L.sort()

left, right = 0, N - 1
answer = sys.maxsize
a1, a2 = 0, 0

while left < right:
    sum_val = L[left] + L[right]

    if abs(sum_val) < answer:
        answer = abs(sum_val)
        a1, a2 = L[left], L[right]

    if sum_val > 0:
        right -= 1
    elif not sum_val:
        a1, a2 = L[left], L[right]
        break
    else:
        left += 1
print(a1, a2)