from itertools import combinations
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
word = [input().rstrip() for _ in range(N)]
if K < 5:
    print(0)
    sys.exit()

necessary = {'a', 'n', 't', 'i', 'c'}
used = [False] * (ord('z') - ord('a') + 1)
for n in necessary:
    used[ord(n) - 97] = True

cand = set([chr(a) for a in range(ord('a'), ord('z') + 1)]) - necessary
K -= 5

answer = 0
for c in combinations(cand, K):
    for alpha in c:
        used[ord(alpha) - 97] = True

    tmp_answer = 0
    for w in word:
        for alpha in w:
            if not used[ord(alpha) - 97]:
                break
        else:
            tmp_answer += 1
    answer = max(answer, tmp_answer)

    for alpha in c:
        used[ord(alpha) - 97] = False
print(answer)