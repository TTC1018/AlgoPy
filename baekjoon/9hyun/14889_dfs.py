import sys
input = sys.stdin.readline


def calc(start, link):
    sum_s, sum_l = 0, 0

    for i in range(N // 2):
        for j in range(N // 2):
            sum_s += S[start[i]][start[j]]
            sum_l += S[link[i]][link[j]]

    return abs(sum_s - sum_l)


def dfs(start, count):
    global answer

    if count == N // 2:
        link = [i for i in range(N) if i not in start]
        answer = min(answer, calc(start, link))

    for i in range(N):
        if i not in start:
            start.append(i)
            dfs(start, count + 1)
            start.remove(i)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
answer = int(1e9)
dfs([], 0)
print(answer)