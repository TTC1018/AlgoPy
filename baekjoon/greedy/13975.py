from heapq import heappush, heappop
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    K = int(input())
    S = list(map(int, input().split()))
    
    S.sort()
    
    answer = 0
    while K > 1:
        a, b = heappop(S), heappop(S)
        answer += (a + b)
        heappush(S, a + b)
        K -= 1
    print(answer)