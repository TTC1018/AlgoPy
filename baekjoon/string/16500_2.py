import sys
input = sys.stdin.readline


def search(idx):
    if idx == s_len:
        print(1)
        sys.exit()

    if not dp[idx]:
        dp[idx] = 1
        for w in word: # 단어들 중에서 일치하는 단어 찾기
            w_len = len(w)
            if s_len - idx >= w_len and w == S[idx:idx+w_len]:
                search(idx + w_len) # 단어 길이만큼 인덱스 건너 뛰기


S = input().rstrip()
s_len = len(S)
N = int(input())
word = [input().rstrip() for _ in range(N)]
dp = [0] * (100 + 1)

search(0)
print(0)