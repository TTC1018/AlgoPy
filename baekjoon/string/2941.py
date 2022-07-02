import sys
input = sys.stdin.readline


S = input().rstrip()
alpha = ['dz=', 'lj', 'nj', 'd-', 's=', 'z=', 'c=', 'c-']

for a in alpha:
    S = S.replace(a, '*')
print(len(S))