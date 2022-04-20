import sys
input = sys.stdin.readline


def tp(pivot, search_list):
    left, right = 0, N - 2
    a1, a2 = search_list[left], search_list[right]
    ideal = abs(search_list[left] + search_list[right] + pivot)

    while left < right:
        temp_sum = search_list[left] + search_list[right] + pivot

        if abs(temp_sum) < ideal:
            a1, a2 = search_list[left], search_list[right]
            ideal = abs(temp_sum)

        if temp_sum < 0:
            left += 1
        elif temp_sum > 0:
            right -= 1
        else:
            break

    answer = sorted([a1, a2, pivot])
    return (ideal, answer)


N = int(input())
L = list(map(int, input().split()))
L.sort()

a_val = sys.maxsize
answer = []
for target in L:
    ti, ta = tp(target, [l for l in L if l != target])
    if ti < a_val:
        a_val = ti
        answer = ta
print(*answer)