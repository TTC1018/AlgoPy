import sys
input = sys.stdin.readline


N = int(input())
answer = 0
posi = []
nega = []
for _ in range(N):
    added = int(input())
    if added == 1:
        answer += 1
    elif added > 1:
        posi.append(added)
    else:
        nega.append(added)
posi.sort(reverse=True)
nega.sort()

p_cnt = len(posi)
if p_cnt > 1:
    if p_cnt % 2 == 1:
        answer += posi[-1]
        p_cnt -= 1
    for i in range(0, p_cnt, 2):
        answer += (posi[i] * posi[i + 1])
elif p_cnt == 1:
    answer += posi[0]

n_cnt = len(nega)
if n_cnt > 1:
    if n_cnt % 2 == 1:
        answer += nega[-1]
        n_cnt -= 1
    for i in range(0, n_cnt, 2):
        answer += (nega[i] * nega[i + 1])
elif n_cnt == 1:
    answer += nega[0]
print(answer)