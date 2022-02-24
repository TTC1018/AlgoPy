N = int(input())
coins = list(map(int, input().split()))

coins.sort()

answer = 1
for c in coins:
    if answer < c:
        break
    answer += c
print(answer)