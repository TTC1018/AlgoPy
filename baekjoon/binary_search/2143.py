T = int(input())
n = int(input())
A = list(map(int, input().split(' ')))
m = int(input())
B = list(map(int, input().split(' ')))

sum_A, sum_B = [0] * 2000000001, [0] * 2000000001
for i in range(1, n + 1):
    for j in range(n - i + 1):
        sum_A[sum(A[j:j+i]) + 1000000000] += 1
for i in range(1, m + 1):
    for j in range(m - i + 1):
        sum_B[sum(B[j:j+i]) + 1000000000] += 1

answer = 0
for val_a in sum_A:
    for val_b in sum_B:
        if val_a + val_b == T:
            answer += (sum_A[val_a + 1000000000] * sum_B[val_b + 1000000000])
print(answer)