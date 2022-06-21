import sys
input = sys.stdin.readline


def btk(s, l):
    if l == s_len:
        if s == S:
            print(1)
            sys.exit()
    if l - 1 == 0:
        return

    if s[-1] == 'A':
        btk(s[:-1], l - 1)

    if s[0] == 'B':
        btk(s[1:][::-1], l - 1)


S = input().rstrip()
T = input().rstrip()
s_len, t_len = len(S), len(T)
btk(T, t_len)
print(0)