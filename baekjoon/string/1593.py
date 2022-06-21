from collections import Counter
import sys
input = sys.stdin.readline


g, s_len = map(int, input().split())
W, S = input().rstrip(), input().rstrip()
cnt_dict = Counter(W) # W를 이루는 문자들의 개수

cnt = 0
counter = Counter(S[:g])
for i in range(s_len - g):
    for key in counter:
        if key not in cnt_dict: # W를 이루는 문자 없으면
            break
        elif cnt_dict[key] != counter[key]: # 문자는 있지만 개수가 다르면
            break
    else: # 조건 다 충족한 경우
        cnt += 1

    # 슬라이드 이동
    counter[S[i]] -= 1 # 맨 앞 문자 제거
    if not counter[S[i]]:
        del counter[S[i]]
    if S[i+g] not in counter:
        counter[S[i+g]] = 0
    counter[S[i+g]] += 1 # 맨 뒤 문자 추가

# 마지막 싸이클
for key in counter:
    if key not in cnt_dict:
        break
    elif cnt_dict[key] != counter[key]:
        break
else:
    cnt += 1
print(cnt)