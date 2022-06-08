from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
oilbank = [list(map(int, input().split())) for _ in range(N)]
L, P = map(int, input().split())

# 주유소에 멈추는 횟수를 최소화 = 연료 많은 주유소를 우선적으로 확인
oilbank.sort(key=lambda x: x[0])

if P >= L:
    print(0)
else:
    answer = 0
    o_idx, o_len = 0, len(oilbank)

    now = 0
    q = []
    while True:
        for i in range(o_idx, o_len):
            if now <= oilbank[i][0] <= P:
                heappush(q, -oilbank[i][1])
            elif oilbank[i][0] > P: # 도달 불가 주유소면 멈추기
                o_idx = i
                break

        if q:
            answer += 1
            now = (P + 1)
            P += (-heappop(q))
        else: # 기름 받을 주유소 없을 때
            break

        if P >= L: # 도착 요건 충족 했을 때
            break

    if P >= L:
        print(answer)
    else:
        print(-1)