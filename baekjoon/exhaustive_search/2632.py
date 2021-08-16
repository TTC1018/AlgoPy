# 시계방향 연속합

P = int(input())
A, B = [], []
m, n = map(int, input().split(' '))
for _ in range(m):
    A.append(int(input()))
for _ in range(n):
    B.append(int(input()))

sum_A, sum_B = [0]*(2000001), [0]*(2000001)
sum_A[0], sum_B[0], sum_A[sum(A)], sum_B[sum(B)] = 1, 1, 1, 1
for i in range(1, m):
    for j in range(m):
        temp_sum = sum(A[i:]) + sum(A[:(i + j) % m]) if j + i > m else sum(A[j:j + i])
        sum_A[temp_sum] += 1

for i in range(1, n):
    for j in range(n):
        temp_sum = sum(B[i:]) + sum(B[:(i + j) % n]) if j + i > n else sum(B[j:j + i])
        sum_B[temp_sum] += 1

answer = 0
for i in range(P+1):
    answer += (sum_A[i] * sum_B[P-i])
print(answer)