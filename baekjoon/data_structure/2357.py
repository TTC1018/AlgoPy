import sys
input = sys.stdin.readline


class Node:
    def __init__(self, left, right):
        self.min = left
        self.max = right

    def __str__(self):
        return f'{self.min} {self.max}'


def generate_tree(left, right, idx):
    if left == right:
        s_tree[idx].min = nums[left]
        s_tree[idx].max = nums[left]
        return s_tree[idx]

    mid = (left + right) // 2
    l_child = generate_tree(left, mid, idx * 2)
    r_child = generate_tree(mid + 1, right, idx * 2 + 1)

    s_tree[idx].min = min(l_child.min, r_child.min)
    s_tree[idx].max = max(l_child.max, r_child.max)
    return s_tree[idx]


def search(start, end, a, b, idx):
    if a > end or b < start:
        return Node(int(1e9), 0)
    if a <= start and b >= end:
        return s_tree[idx]

    mid = (start + end) // 2
    left = search(start, mid, a, b, idx * 2)
    right = search(mid + 1, end, a, b, idx * 2 + 1)

    return Node(min(left.min, right.min), max(left.max, right.max))

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
s_tree = [Node(int(1e9), 0) for _ in range(N*4)]
generate_tree(0, N - 1, 1)

answer = []
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())
    answer.append(search(0, N - 1, A, B, 1))
print('\n'.join(map(str, answer)))
