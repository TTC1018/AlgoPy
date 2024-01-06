import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n, K = map(int, input().split())
    nums = sorted(map(int, input().split()))

    answer = 0
    answer_diff = int(1e9)
    l, r = 0, n - 1
    while l < r:
        diff = nums[l] + nums[r]
        diff_abs = abs(diff - K)

        if diff_abs == answer_diff:
            answer += 1
        elif diff_abs < answer_diff:
            answer = 1
            answer_diff = diff_abs

        if diff == K:
            l, r = l + 1, r - 1
        elif diff < K:
            l += 1
        elif diff > K:
            r -= 1
    ans.append(answer)
print('\n'.join(map(str, ans)), end='')
