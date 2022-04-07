from copy import deepcopy


def all_heard():
    for i in range(N):
        if not visited[i]:
            return False
    return True


def call(now, count, nexts):
    global answer
    
    if all_heard():
        answer = min(answer, count)
        return
    
    for next in c_list[now]:
        if not visited[next]:
            visited[next] = True
            call(next, count + 1, [n for n in nexts if not visited[n] and n != now])


N = int(input())
childs = list(map(int, input().split()))
c_list = [[] for _ in range(N)]
for i in range(1, N):
    c_list[childs[i]].append(i)
visited = [False] * N


answer = int(1e9)
visited[0] = True
call(0, 1, list())
print(answer)