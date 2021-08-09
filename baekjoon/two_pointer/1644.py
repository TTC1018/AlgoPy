#에라토스테네스의 체
N = int(input())

a = [False, False] + [True] * (N-1)
primes = []
for i in range(2, N + 1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N + 1, i):
            a[j] = False

answer = 0
left, right = 0, 0
while right <= len(primes):
    temp_sum = sum(primes[left:right])
    if temp_sum == N:
        answer += 1
        right += 1
    elif temp_sum < N:
        right += 1
    else:
        left += 1

print(answer)