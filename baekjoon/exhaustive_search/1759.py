from itertools import combinations
from collections import deque

# L개의 알파벳으로 구성되는 단어, 최소 1개의 (a e i o u)와 최소 두개의 자음, 알파벳 오름차순
L, C = list(map(int, input().split(' ')))
alphas = input().split(' ')
vo_ = ['a', 'e', 'i', 'o', 'u']
vowel = [alpha for alpha in alphas if alpha in vo_]
conso = [alpha for alpha in alphas if alpha not in vo_]

answer = []
q = deque()
for v in vowel:
    q.append([v])

while q:
    w = q.popleft()

    if len(w) == L:
        answer.append(w)
        continue

    if L - len(w) > 2:
        for rv in [[rv] for rv in vowel if rv not in w]:
            temp_w_rv = sorted(w + rv)
            if temp_w_rv not in q:
                q.append(temp_w_rv)

    perm = list(combinations(conso, L - len(w)))
    for p in perm:
        temp_w_p = sorted(w + list(p))
        if temp_w_p not in q:
            q.append(temp_w_p)

for i in range(len(answer)):
    answer[i] = ''.join(answer[i])

answer = sorted(list(set(answer)))
for word in answer:
    print(word)