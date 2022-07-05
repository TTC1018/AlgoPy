from collections import defaultdict
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
R = list(map(int, input().split()))
plugged = dict()
cnt_dict = defaultdict(int)
for r in R:
    cnt_dict[r] += 1

plug = []
answer = 0
p_cnt = 0
# 앞으로 횟수 많이 남은 물건 남기기
for i in range(K):
    if p_cnt < N:
        if R[i] not in plugged:
            p_cnt += 1
            plugged[R[i]] = True
    else:
        if R[i] not in plugged: # 안 꽂혀 있는 상태면
            answer += 1
            removal = -1
            for key in plugged:
                if not cnt_dict[key]: # 앞으로 안 나오는 물건이라면
                    removal = key
                    break
            else: # 다들 나올 가능성이 있으면
                farthest = -1
                for key in plugged:
                    for j in range(i + 1, K):
                        if R[j] == key:
                            farthest = max(farthest, j)
                            break
                del plugged[R[farthest]] # 가장 나중에 사용하는 물건 빼기

            if removal != -1:
                del plugged[removal]

            plugged[R[i]] = True  # 꽂았다고 표시
    cnt_dict[R[i]] -= 1
print(answer)