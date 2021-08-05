from itertools import permutations
from collections import deque

L, C = list(map(int, input().split(' ')))
alphas = input().split(' ')
vowel = []
conso = []

for alpha in alphas:
    if alpha in ['a', 'e', 'i', 'o', 'u']:
        vowel.append(alpha)
    else:
        conso.append(alpha)
vowel.sort()
conso.sort()
# L개의 알파벳으로 구성되는 단어, 최소 1개의 (a e i o u)와 최소 두개의 자음, 알파벳 오름차순
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
        rest_v = [v for v in vowel if v not in w]
        for rv in rest_v:
            if w[-1] < rv:
                q.append(w + [rv])
    else:
        perm = list(map(list, list(permutations(conso, L - len(w)))))
        for p in perm:
            p.sort()

        for p in perm:
            if perm.count(p) > 1:
                perm.remove(p)
        print(perm)
        perm = list(set(perm))

        for p in perm:
            if w[-1] < p[0]:
                q.append(w + list(p))


for i in range(len(answer)):
    answer[i] = ''.join(answer[i])

answer = list(set(answer))
answer.sort()

for word in answer:
    print(word)
