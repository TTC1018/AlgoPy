N, K = map(int, input().split(' '))

answer = 0
while N > 1:
    if N % K == 0:
        N //= K
        answer += 1
    else:
        N -= 1
        answer +=1
print(answer)
