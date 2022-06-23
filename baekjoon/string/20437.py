from collections import defaultdict
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    W = input().rstrip()
    K = int(input())

    w_len = len(W)
    cnt_dict = defaultdict(list)
    for i in range(w_len):
        cnt_dict[W[i]].append(i) # 문자 W[i]가 어느 인덱스에 위치하는지 기록

    cand = {key:cnt_dict[key] for key in cnt_dict if len(cnt_dict[key]) >= K}
    if not cand:
        print(-1)
        continue

    a1, a2 = sys.maxsize, 0
    for key in cand:
        c_len = len(cand[key])
        for i in range(c_len - K + 1):
            left, right = cand[key][i], cand[key][i + K - 1]
            a1 = min(a1, right - left + 1)
            a2 = max(a2, right - left + 1)
    print(a1, a2)