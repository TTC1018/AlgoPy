import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def search_p(start):
    parent.add(start)
    if graph[start] == -1:
        return
    search_p(graph[start])


def search_p2(start):
    if graph[start] in parent:
        print(graph[start])
        return
    search_p2(graph[start])



for _ in range(int(input())):
    N = int(input())
    graph = [-1 for _ in range(N + 1)]
    for _ in range(N - 1):
        p, c = map(int, input().split())
        graph[c] = p

    parent = set()
    A, B = map(int, input().split())
    search_p(A)
    search_p2(B)