import sys
input = sys.stdin.readline


N = int(input())
S = [input().rstrip() for _ in range(N)]

answer = 0
for word in S:
    prev = word[0]
    w_len = len(word)
    memo = dict()
    memo[prev] = True
    for i in range(1, w_len):
        if prev == word[i]:
            continue
        else:
            if word[i] not in memo:
                memo[word[i]] = True
                prev = word[i]
            else:
                break
    else:
        answer += 1
print(answer)