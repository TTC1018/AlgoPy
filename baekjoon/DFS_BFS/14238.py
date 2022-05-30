import sys
input = sys.stdin.readline


def dfs(a, b, c, one, two):
    global answer
    if (a, b, c) == (a_cnt, b_cnt, c_cnt):
        print(''.join(answer))
        return True

    if a < a_cnt:
        answer[a + b + c] = 'A'
        if not dp[a + 1][b][c][A][one]:
            dp[a + 1][b][c][A][one] = True
            if dfs(a + 1, b, c, A, one):
                return True
    if b < b_cnt:
        answer[a + b + c] = 'B'
        if one != B: # 이전 글자 확인
            if not dp[a][b + 1][c][B][one]:
                dp[a][b + 1][c][B][one] = True
                if dfs(a, b + 1, c, B, one):
                    return True
    if c < c_cnt:
        answer[a + b + c] = 'C'
        if C not in [one, two]: # 이전, 이이전 글자 확인
            if not dp[a][b][c + 1][C][one]:
                dp[a][b][c + 1][C][one] = True
                if dfs(a, b, c + 1, C, one):
                    return True
    return False


S = list(input())
a_cnt = S.count('A')
b_cnt = S.count('B')
c_cnt = S.count('C')
total = a_cnt + b_cnt + c_cnt

dp = [[[[[False] * 3 for _ in range(3)] for _ in range(c_cnt + 1)] for _ in range(b_cnt + 1)] for _ in range(a_cnt + 1)]
A, B, C = 0, 1, 2
answer = [''] * (total + 1)
dp[0][0][0][A][A] = True
if not dfs(0, 0, 0, A, A):
    print(-1)