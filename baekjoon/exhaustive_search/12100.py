from collections import deque

N = int(input())
B = []
for i in range(N):
    B.append(list(map(int, input().split(' '))))

# 가능한 경우의 수 : 상 하 좌 우
q = deque()
q.append((B, 0))

while q:
    temp_B, count = q.popleft()

    #상
    for i in range(N):
        
    #하

    #좌

    #우