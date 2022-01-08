N = int(input())

d = dict()
for i in range(N):
    name, score = input().split()
    d[name] = int(score)

answer = sorted(d.items())
for n in answer:
    print(n[0], end=' ')