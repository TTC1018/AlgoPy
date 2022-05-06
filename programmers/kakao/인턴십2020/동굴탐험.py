from collections import deque


def solution(n, path, order):
    	
    graph = [[] for _ in range(n)]
    for A, B in path:
        graph[A].append(B)
        graph[B].append(A)
      
    orders =[0] * n
    for A, B in order:
        orders[B] = A
    
    count = 0
    visited = [False] * n
    q = deque()
    q.append(0)
    save = dict()
    
    while q:
        now = q.popleft()
        
        # 미방문한 선행 방이 있을 때
        if orders[now] and not visited[orders[now]]:
            save[orders[now]] = now
            continue
        
        visited[now] = True
        count +=1
    	
        for nxt in graph[now]:
            if not visited[nxt]:     
                q.append(nxt)
        
        # 선행 완료 됐을 때
        if now in save:
            q.append(save[now]) # 못 간 방 추가
                    
    return n == count