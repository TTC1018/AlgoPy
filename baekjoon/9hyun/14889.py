from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
answer = int(1e9)

cands = list(combinations([i for i in range(N)], N // 2))
for i in range(len(cands) // 2):

    start_sum = 0
    for c in cands[i]:
        for other_c in cands[i]:
            start_sum += S[c][other_c]

    link_sum = 0
    for c in cands[-i - 1]: # combinations으로 조합을 짜면, 인덱스 i 집합과 인덱스 -i - 1 집합은 여집합 관계이다.
        for other_c in cands[-i - 1]:
            link_sum += S[c][other_c]

    answer = min(answer, abs(start_sum - link_sum))
print(answer)