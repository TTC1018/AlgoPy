from collections import defaultdict
import sys
input = sys.stdin.readline


name = input().rstrip()
d = defaultdict(int)
for s in name:
    d[s] += 1

n_len = len(name)
if not n_len % 2:
    for key in d:
        if d[key] % 2:
            print('I\'m Sorry Hansoo')
            break
    else:
        S = ''
        for key in sorted(d.keys()):
            S += (key * (d[key] // 2))
        print(S + S[::-1])
else:
    cnt = 0
    odd = ''
    for key in d:
        if d[key] % 2:
            odd = key
            if cnt:
                print('I\'m Sorry Hansoo')
                break
            cnt += 1
    else:
        S = ''
        for key in sorted(d.keys()):
            S += (key * (d[key] // 2))
        print(S + odd + S[::-1])
