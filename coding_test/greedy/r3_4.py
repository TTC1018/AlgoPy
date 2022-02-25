N = int(input())
coins = list(map(int, input().split()))

coins.sort()

answer = 1 # 가장 작은 수부터 가능한 지 확인
for c in coins:
    if answer < c: # 커버 불가능할 때
        break
    answer += c # 커버 한계를 상향시킴 (현재 동전들로 가능한 커버 한계 + 1 값으로 유지됨)

print(answer)