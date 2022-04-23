import sys
input = sys.stdin.readline


q = int(input())
name = dict()
for _ in range(q):
    s, p = input().split()
    if not name.get(s):
        name[s] = [0, 0]
    if p == '+':
        name[s][0] += 1
    elif p == '-':
        if name[s][0] > 0:
            name[s][0] -= 1
        else:
            name[s][1] += 1

answer = 0
for n in name:
    answer += sum(name[n])
print(answer)