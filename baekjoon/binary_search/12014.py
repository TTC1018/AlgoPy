from bisect import bisect_left
import sys
input = sys.stdin.readline


for case in range(int(input())):
    N, K = map(int, input().split())
    stocks = list(map(int, input().split()))

    sequence = [-1]
    for i in range(N):
        if sequence[-1] < stocks[i]:
            sequence.append(stocks[i])
        else:
            idx = bisect_left(sequence, stocks[i])
            sequence[idx] = stocks[i]
    sequence.pop(0)

    print('Case #{}'.format(case + 1))
    if len(sequence) >= K:
        print(1)
    else:
        print(0)