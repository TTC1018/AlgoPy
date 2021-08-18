# defaultdict는 

T = int(input())
n = int(input())
A = list(map(int, input().split(' ')))
m = int(input())
B = list(map(int, input().split(' ')))

sum_A, sum_B = {}, {}
for i in range(1, n + 1):
    for j in range(n - i + 1):
        sum_A[sum(A[j:j+i])] = sum_A.get(sum(A[j:j+i]), 0) + 1
for i in range(1, m + 1):
    for j in range(m - i + 1):
        sum_B[sum(B[j:j+i])] = sum_B.get(sum(B[j:j+i]), 0) + 1

answer = 0
for val_a in sum_A:
    answer += (sum_A[val_a] * sum_B.get(T-val_a, 0))
print(answer)