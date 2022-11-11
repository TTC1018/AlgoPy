import sys
input = sys.stdin.readline

N = int(input())
N_to_binary = bin(N)[2:]

answer = 0
length = len(N_to_binary)
for i in range(length):
    if N_to_binary[i] == '1':
        answer += 3**(length - i - 1)
print(answer)