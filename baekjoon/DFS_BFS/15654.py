import sys
input = sys.stdin.readline


def search(idxs, count):
    if count == M:
        for idx in idxs:
            print(nums[idx], end=' ')
        print()
        return

    for nxt in [i for i in range(N) if i not in idxs]:
        search(idxs + [nxt], count + 1)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for i in range(N):
    search([i], 1)