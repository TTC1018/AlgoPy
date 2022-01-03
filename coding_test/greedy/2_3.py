N, M = map(int, input().split(' '))

answer = 0

for i in range(N):
    temp = min(map(int, input().split(' ')))
    answer = max(answer, temp)

print(answer)

