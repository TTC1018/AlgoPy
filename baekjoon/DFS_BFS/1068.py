import sys
input = sys.stdin.readline


def search(node):
    global answer

    if node == R:
        return

    if not T[node] or (len(T[node]) == 1 and T[node][0] == R):
        answer += 1
        return

    for nxt in T[node]:
        search(nxt)



N = int(input())
T = [[] for _ in range(N)] # 자식 노드 기록

start = -1
parent = list(map(int, input().split()))
for i in range(N):
    if parent[i] != -1:
        T[parent[i]].append(i)
    else:
        start = i
R = int(input())

answer = 0
search(start)
print(answer)