import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(number, count):
    if count == 4:
        print(1)
        sys.exit()

    for nxt in F[number]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, count + 1)
            visited[nxt] = False




N, M = map(int, input().split())
F = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    F[a].append(b)
    F[b].append(a)


for num in range(N):
    visited = [False] * N
    visited[num] = True
    dfs(num, 0)
print(0)