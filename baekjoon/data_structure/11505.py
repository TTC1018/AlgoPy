import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
MOD = 1000000007


def generate_tree(start, end, idx):
    if start == end:
        s_tree[idx] = nums[start]
        return s_tree[idx]

    mid = (start + end) // 2
    s_tree[idx] = generate_tree(start, mid, idx * 2) * generate_tree(mid + 1, end, idx * 2 + 1) % MOD
    return s_tree[idx]


def range_mul(now_s, now_e, left, right, idx):
    if now_s > right or now_e < left:
        return 1
    if left <= now_s and now_e <= right:
        return s_tree[idx]

    mid = (now_s + now_e) // 2
    return range_mul(now_s, mid, left, right, idx * 2) * range_mul(mid + 1, now_e, left, right, idx * 2 + 1) % MOD


def update(start, end, node, new, idx):
    if start <= node <= end:
        if start == end:
            s_tree[idx] = new
            return

        mid = (start + end) // 2
        update(start, mid, node, new, idx * 2)
        update(mid + 1, end, node, new, idx * 2 + 1)
        s_tree[idx] = s_tree[idx * 2] * s_tree[idx * 2 + 1] % MOD


N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
s_tree = [0] * (N * 4)
generate_tree(0, N - 1, 1)

answer = []
for _ in range(M + K):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        update(0, N - 1, b, c, 1)
        nums[b] = c
    elif a == 2:
        answer.append(range_mul(0, N - 1, b, c - 1, 1))
print('\n'.join(map(str, answer)))