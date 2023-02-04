from math import ceil, sqrt
import sys
input = sys.stdin.readline

# 세그먼트 트리
def generate_tree(left, right, idx):
    if left == right:
        s_tree[idx] = nums[left]
        return s_tree[idx]

    mid = (left + right) // 2
    s_tree[idx] = generate_tree(left, mid, idx * 2) + generate_tree(mid + 1, right, idx * 2 + 1)
    return s_tree[idx]


def range_sum(now_s, now_e, left, right, idx):
    if right < now_s or left > now_e:
        return 0
    if left <= now_s and right >= now_e:
        return s_tree[idx]

    mid = (now_s + now_e) // 2
    return range_sum(now_s, mid, left, right, idx * 2) + range_sum(mid + 1, now_e, left, right, idx * 2 + 1)


def update_tree(start, end, node, val_diff, idx):
    if start <= node <= end:
        s_tree[idx] += val_diff
        if start != end:
            mid = (start + end) // 2
            update_tree(start, mid, node, val_diff, idx * 2)
            update_tree(mid + 1, end, node, val_diff, idx * 2 + 1)


N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
s_tree = [0] * (N * 4)
generate_tree(0, N - 1, 1)

answer = []
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update_tree(0, N - 1, b - 1, c - nums[b - 1], 1)
        nums[b - 1] = c
    elif a == 2:
        answer.append(range_sum(0, N - 1, b - 1, c - 1, 1))
print('\n'.join(map(str, answer)))