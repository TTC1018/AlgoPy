import sys
input = sys.stdin.readline

def search(nums, count):
    if count == M:
        print(*nums)
        return

    for nxt in range(nums[-1] + 1, N + 1):
        search(nums + [nxt], count + 1)

N, M = map(int, input().split())
for i in range(1, N + 1):
    search([i], 1)