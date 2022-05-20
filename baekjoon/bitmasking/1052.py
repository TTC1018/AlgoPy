N, K = map(int, input().split())

bottle = [1] * K
rest = N - K

answer = 0
while True:
    binary = bin(N)[2:]
    b_cnt = binary.count('1')
    if b_cnt <= K:
        print(answer)
        break

    N += 1
    answer += 1