from collections import deque


def solve(A, B):
    q = deque([[A, '']])

    visited = [False] * 10000
    visited[A] = True
    while q:
        num, solution = q.popleft()

        if num == B:
            print(solution)
            return

        D = (num * 2) % 10000
        if not visited[D]:
            visited[D] = True
            q.append([D, solution + "D"])

        S = (num - 1) % 10000 if num != 0 else 9999
        if not visited[S]:
            visited[S] = True
            q.append([S, solution + "S"])

        L = (num % 1000) * 10 + num // 1000
        if not visited[L]:
            visited[L] = True
            q.append([L, solution + "L"])

        R = (num % 10) * 1000 + (num // 10)
        if not visited[R]:
            visited[R] = True
            q.append([R, solution + "R"])


T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    solve(A, B)