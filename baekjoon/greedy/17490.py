import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
S = [-1] + list(map(int, input().split()))
if M in [0, 1]:
    print('YES')
    sys.exit()

area = [-1] * (N + 1)
B = [tuple(map(int, input().split())) for _ in range(M)]
B.sort()

# 구역 표시
for i, j in B:
    area[i] = i
    for idx in range(i - 1, 0, -1):
        if area[idx] == -1:
            area[idx] = i
        else:
            break

# 원형이므로, 1과 N 사이에 공사지역 없다면 같은 구역으로 표시해야 됨
if B[-1][0] != N:
    for i in range(B[-1][1], N + 1):
        area[i] = area[1]

# 각 구역은 연결되어 있으므로, 구역 중에 하나만 섬에 연결하면 됨
# 즉, 구역 내에 속한 돌 소요값 중 최소값 찾아내서 더함

# area[1]로 표시된 구역 중에 가장 작은 돌 요구값 구하기
min_val = S[1]
p_num = area[1]
idx = 2
while idx < N + 1 and area[idx] == p_num:
    min_val = min(min_val, S[idx])
    idx += 1
nxt = idx
idx = N
while idx >= 0 and area[idx] == p_num:
    min_val = min(min_val, S[idx])
    idx -= 1

# 다른 구역들의 최소 돌 요구값 구하기
answer = min_val
while nxt < N + 1 and area[nxt] != area[1]:
    p_num = area[nxt]
    min_val = int(1e9)
    for idx in range(nxt, N + 1):
        if area[idx] == p_num:
            min_val = min(min_val, S[idx])
        else:
            nxt = idx
            break
    else:
        nxt = N + 1
    answer += min_val

if answer <= K:
    print('YES')
else:
    print('NO')
