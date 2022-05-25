import sys
input = sys.stdin.readline


def search(idx, prev_p):
    global S

    now = T[idx] # S의 idx번째 문자
    cnt = 0
    S += now

    for i in range(idx, t_len, prev_p + 1): # 이전 패턴의 길이 만큼 넘기면서 S의 idx번째 문자가 몇개 있나 확인
        if T[i] == now:
            cnt += 1
        else: # 다른 문자 출현하면 break
            nxt_idx = i
            break
    else: # break 없이 T의 길이 넘어섰을 때 = 마지막 문자를 탐색한 것
        nxt_idx = t_len # 더이상 탐색 못 하도록 값 할당

    if nxt_idx < t_len: # 더 탐색할 문자가 있을 때
        A.append(cnt)
        search(nxt_idx, nxt_idx)


T = input()
t_len = len(T)
S = ''
A = []

# 첫번째 패턴 찾기
f_cnt = 1
for i in range(1, t_len):
    if T[i] == T[0]:
        f_cnt += 1
    else:
        break

S += T[0]
A.append(f_cnt)

if f_cnt < t_len:
    search(f_cnt, f_cnt)
print(S)
print(*A)