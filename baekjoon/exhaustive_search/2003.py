N, M = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))

answer = 0
for i in range(1, N + 1): # 1 2 3 ... 10
    for j in range((N - i) + 1): # 0~9 0~8 0~7... 0
        temp = 0
        while temp < M:
            for k in range(j, j + i):
                temp += A[j]
            break
        if temp == M:
            answer += 1

print(answer)