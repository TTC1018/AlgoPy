s = input()

jaeum = {'q', 'w', 'e', 'r', 'R', 't', 'T',
         'a', 's', 'd', 'f', 'g',
         'z', 'x', 'c', 'v'}
moeum = {'y', 'u', 'i', 'o', 'O', 'p', 'P',
         'h', 'j', 'k', 'l',
         'b', 'n', 'm'}
d_jaeum = {'rt', 'sw', 'sg', 'fr', 'fa',
           'fq', 'ft', 'fx', 'fv', 'fg', 'qt'}

s_len = len(s)
answer = 0
for i in range(1, s_len - 2):
    if s[i - 1] in moeum and s[i] in jaeum and s[i + 1] in moeum:
        answer += 1
    elif s[i - 1] in moeum and s[i:i+2] in d_jaeum and s[i + 2] in moeum:
        answer += 1

if s[-3] in moeum and s[-2] in jaeum and s[-1] in moeum:
    answer += 1
print(answer)