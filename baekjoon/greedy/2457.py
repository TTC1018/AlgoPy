import sys


N = int(input())
flower = [tuple(map(int, input().split())) for _ in range(N)]
flower.sort(key=lambda x:(x[0], x[1]))

answer = 0
memo = [3, 1, 0, 0]
for i in range(N):
    fsm, fsd, fem, fed = flower[i]
    if fsm < memo[0] or (fsm == memo[0] and fsd <= memo[1]): # 이전 꽃과 시기가 겹칠 수 있는 꽃일 때
        if memo[2] <= fem and memo[3] <= fed:
            answer += 1
            memo = flower[i]
            if memo[2] > 11 or (memo[2] == 11 and memo[3] == 30):
                break
    else:
        print(0)
        sys.exit()
print(answer)