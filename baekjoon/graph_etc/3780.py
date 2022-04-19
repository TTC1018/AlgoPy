import sys
input = sys.stdin.readline
def find_parent(node):
    if parent[node] == node:
        return node
    
    new_parent = find_parent(parent[node]) # 최종 부모
    dist[node] += dist[parent[node]] # 부모까지 거치는 길이 누적하기
    parent[node] = new_parent
    return parent[node]


def union_parent(a, b):
    dist[a] = abs(a - b) % 1000
    parent[a] = b


for _ in range(int(input())):
    N = int(input())
    parent = [i for i in range(N + 1)]
    dist = [0 for _ in range(N + 1)] # 특정 기업에서 센터까지의 길이
    while True:
        data = input().split()
        op = data[0]

        if op == 'O':
            break
        elif op == 'E':
            I = int(data[1])
            find_parent(I) # 최종 부모로 갱신
            print(dist)
            print(dist[I])
            
        elif op == 'I':
            I, J = map(int, data[1:]) 
            # I는 부모, J는 특정 부모의 자식
            # J의 부모에 union
            union_parent(I, J)