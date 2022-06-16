from collections import deque
import sys
input = sys.stdin.readline


for i in range(int(input())):
    A, B, C = input().rstrip().split()
    a_len, b_len, c_len = len(A), len(B), len(C)
    visited = [[False] * (b_len + 1) for _ in range(a_len + 1)]

    answer = 'no'
    q = deque()
    q.append(('', 0, 0, 0))

    while q:
        s, a_idx, b_idx, c_idx = q.popleft()
        if c_idx == c_len:
            if s == C:
                answer = 'yes'
                break
            continue


        if a_idx < a_len and A[a_idx] == C[c_idx]:
            if not visited[a_idx + 1][b_idx]:
                visited[a_idx + 1][b_idx] = True
                q.append((s + C[c_idx], a_idx + 1, b_idx, c_idx + 1))
        if b_idx < b_len and B[b_idx] == C[c_idx]:
            if not visited[a_idx][b_idx + 1]:
                visited[a_idx][b_idx + 1] = True
                q.append((s + C[c_idx], a_idx, b_idx + 1, c_idx + 1))

    print('Data set {}: {}'.format(i + 1, answer))