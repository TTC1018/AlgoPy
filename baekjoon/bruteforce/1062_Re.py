from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
word = [input().rstrip() for _ in range(N)]
if K < 5:
    print(0)
    sys.exit()
K -= 5

necessary = set('antic')
to_be_covered = []
cand = set()

covered_by_n = 0
for w in word:
    tmp = set(w) - necessary # 필수 알파벳 제외 필요한 알파벳

    if tmp:
        to_be_covered.append(tmp)
        cand.update(tmp)
    else:
        covered_by_n += 1 # 기본 알파벳으로 커버 가능
if len(cand) <= K: # 커버해야 되는 알파벳이 K개 이하임
    print(N)
    sys.exit()

answer = 0
for c in combinations(cand, K):
    target = set(c)
    tmp_answer = 0
    for tbc in to_be_covered:
        if target >= tbc: # 커버될 때
            tmp_answer += 1
    answer = max(answer, tmp_answer)
print(answer + covered_by_n)