import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

# T를 역행시켜 답을 찾아내기
s_len, t_len = len(S), len(T)
while s_len <= t_len:

    if s_len == t_len:
        if S == T:
            print(1)
            sys.exit()

    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]
    t_len -= 1
print(0)