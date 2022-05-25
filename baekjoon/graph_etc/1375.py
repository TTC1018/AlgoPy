# from collections import deque, defaultdict
# import sys
# input = sys.stdin.readline
#
#
# def find_parent(node):
#     if parent[node] == node:
#         return node
#
#     parent[node] = find_parent(parent[node])
#     return parent[node]
#
#
# def union_parent(a, b):
#     pa = find_parent(a)
#     pb = find_parent(b)
#     parent[pb] = pa
#
#
# N, M = map(int, input().split())
# parent = dict()
# graph_dict = defaultdict(list)
# indegree_dict = defaultdict(int)
# for _ in range(M):
#     a, b = input().split()
#     if a not in parent:
#         parent[a] = a
#     if b not in parent:
#         parent[b] = b
#
#     union_parent(a, b)
#     graph_dict[a].append(b)
#     indegree_dict[b] += 1
#     if not indegree_dict[a]:
#         continue
#
# q = deque()
# for k in indegree_dict:
#     if not indegree_dict[k]:
#         q.append(k)
# age = []
# vague = defaultdict(list)
# while q:
#     now = q.popleft()
#     age.append(now)
#     idk = []
#     for nxt in graph_dict[now]:
#         indegree_dict[nxt] -= 1
#         if not indegree_dict[nxt]:
#             q.append(nxt)
#             idk.append(nxt)
#
#     if len(idk) > 1:
#         vague[find_parent(now)].append(tuple(idk))
#
# Q = int(input())
# answer = []
# for _ in range(Q):
#     a, b = input().split()
#     if a not in parent:
#         parent[a] = a
#     if b not in parent:
#         parent[b] = b
#
#     if find_parent(a) != find_parent(b):
#         answer.append('gg')
#     else:
#         for l in vague[find_parent(a)]:
#             if a in l and b in l:
#                 answer.append('gg')
#                 break
#         else:
#             answer.append(age[min(age.index(a), age.index(b))])
# print(*answer)



######################################
import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def bfs(x):
    q = deque()
    q.append(x)

    A, V = [], defaultdict(int)
    while q:
        v = q.popleft()
        A.append(v)

        for nxt in graph[v]:
            if not V[nxt]:
                V[nxt] = 1
                q.append(nxt)

    return A


N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    a, b = input().split()
    graph[b].append(a)

answer = []
for _ in range(int(input())):
    x, y = input().split()
    if x == y:
        answer.append("gg")
    elif y in bfs(x):
        answer.append(y)
    elif x in bfs(y):
        answer.append(x)
    else:
        answer.append("gg")
print(*answer)