import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def bruteforce(total):
    global cnt
    if total > n:
        return

    if total == n:
        cnt += 1
        if cnt == k:
            print('+'.join(map(str, nums)))
            exit()
        return

    for added in range(1, 3 + 1):
        nums.append(added)
        bruteforce(total + added)
        nums.pop()

n, k = map(int, input().split())
nums = []
cnt = 0
bruteforce(0)
print(-1)