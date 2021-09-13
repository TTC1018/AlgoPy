N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 총감독관 1명 = B, 부감독관 X명 = C*X

answer = 0
for i in range(N):
    first = A[i] - B
    answer += 1

    if first > 0:
        answer += first // C if (first % C) == 0 else first // C + 1

print(answer)