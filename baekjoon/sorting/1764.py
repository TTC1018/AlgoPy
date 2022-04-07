N, M = map(int, input().split())

D, B = {}, {}
for _ in range(N):
    D[input()] = True
for _ in range(M):
    B[input()] = True

answer = []
for d in D:
    if d in B:
        answer.append(d)
print(len(answer))
answer.sort()
for a in answer:
    print(a)