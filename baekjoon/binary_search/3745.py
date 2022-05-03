from bisect import bisect_left
import sys
input = sys.stdin.readline


while True:
    try:
        N = int(input())
        P = list(map(int, input().split()))

        sequence = [-1]
        for i in range(N):
            if sequence[-1] < P[i]:
                sequence.append(P[i])
            else:
                idx = bisect_left(sequence, P[i])
                sequence[idx] = P[i]
        sequence.pop(0)
        print(len(sequence))
    except:
        break