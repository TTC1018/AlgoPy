import sys

def dfs(now):
    for nxt in range(N):
        if KUBC[now][nxt] and not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)
            answer.append(nxt + 1)


N = int(sys.stdin.readline())
KUBC = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N

answer = []
visited[0] = True
dfs(0)
answer.append(1)
answer.reverse()

print(len(answer))
print(*answer)