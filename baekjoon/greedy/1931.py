N = int(input())
M = [tuple(map(int, input().split())) for _ in range(N)]
M.sort(key=lambda x:(x[1], x[0]))

answer = 1
end = M[0][1]
for i in range(1, N):
    if M[i][0] >= end:
        end = M[i][1]
        answer += 1
print(answer)