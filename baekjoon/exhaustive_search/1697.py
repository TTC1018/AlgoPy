from collections import deque

N, K = [int(''.join(n)) for n in input().split(' ')]
visited = [0] * 100001


def solve():
    q = deque()
    q.append(N)

    while q:
        X = q.popleft()
        if X == K:
            print(visited[X])
            break
        for next in [X-1, X+1, X*2]:
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = visited[X] + 1
                q.append(next)


solve()
