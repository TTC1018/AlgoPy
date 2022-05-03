from itertools import combinations
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    tot_x, tot_y = 0, 0
    
    pos = []
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        tot_x += x
        tot_y += y
        pos.append((x, y))
    
    answer = sys.maxsize
    # 점의 반이 시작점이면, 나머지 반은 끝점이므로
    # 시작점만 조합으로 구하면 끝점은 구할 필요가 없음
    starts = list(combinations(pos, N // 2)) 
    for s in starts:
        tot_x1, tot_y1 = 0, 0
        # 시작점 합
        for cand in s:
            tot_x1 += cand[0]
            tot_y1 += cand[1]
        
        # 끝점 총합
        tot_x2 = tot_x - tot_x1
        tot_y2 = tot_y - tot_y1
        
        # 벡터값 계산
        sum_val = ((tot_x1 - tot_x2)**2 + (tot_y1 - tot_y2)**2)**(1/2)
        answer = min(answer, sum_val) # 최소값 갱신
    print('{0:.12f}'.format(answer))