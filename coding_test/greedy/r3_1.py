N = int(input())
people = list(map(int, input().split()))

people.sort()
answer = 0

temp = 0
for p in people:
    temp += 1

    if p >= temp:
        answer += 1
        temp = 0
print(answer)