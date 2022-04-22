from heapq import heappop, heappush
import sys
input = sys.stdin.readline
            

N, K = map(int, input().split())
J = [tuple(map(int, input().split())) for _ in range(N)] # (무게, 가격)
C = [int(input()) for _ in range(K)] # 가방이 담을 수 있는 무게 한계치

J.sort()
C.sort()
q = []
answer = 0
w_idx = 0
for i in range(K):
    while w_idx < N and J[w_idx][0] <= C[i]:
        heappush(q, -J[w_idx][1]) # MaxHeap 이므로 음수로 push
        w_idx += 1

    if len(q) != 0:
        answer += -heappop(q) # MaxHeap 이므로 음수로 pop
print(answer)