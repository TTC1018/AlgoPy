import sys
input = sys.stdin.readline


N = int(input())
R = list(map(int, input().split()))
O = list(map(int, input().split()))


standard, s_idx = O[0], 0
answer= 0
for i in range(1, N - 1):
    if O[i] <= standard:
        answer += (standard * sum(R[s_idx:i]))
        standard, s_idx = O[i], i
answer += (standard * sum(R[s_idx:N]))

print(answer)