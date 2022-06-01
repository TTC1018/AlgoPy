import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
box = [tuple(map(int, input().split())) for _ in range(M)]
box.sort(key= lambda x:x[1])

answer = 0
cap = [C] * (N + 1)
for bs, be, bn in box:
    tmp_cap = C
    for i in range(bs, be): # 시작 지점 ~ 도착 지점 사이의 가장 낮은 박스 수용값 (가능한 만큼만 상차)
        tmp_cap = min(tmp_cap, cap[i])
    tmp_cap = min(tmp_cap, bn) # 박스값과 최소 수용값 비교

    for i in range(bs, be): # 시작 지점부터 도착 지점까지 수용값 빼주기
        cap[i] -= tmp_cap
    answer += tmp_cap
print(answer)