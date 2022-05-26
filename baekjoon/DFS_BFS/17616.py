import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline


def search_better(num):
    checked[num] = True
    result = 1
    for nxt in better[num]:
        if not checked[nxt]:
            result += search_better(nxt)
    return result

def search_worse(num):
    checked[num] = True
    result = 1
    for nxt in worse[num]:
        if not checked[nxt]:
            result += search_worse(nxt)
    return result


N, M, X = map(int, input().split())
worse = [[] for _ in range(N + 1)]
better = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    worse[A].append(B)
    better[B].append(A)

checked = [False] * (N + 1)
U = search_better(X)
V = N - search_worse(X) + 1
print(U, V)