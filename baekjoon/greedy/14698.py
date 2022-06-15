from heapq import heappush, heappop
import sys
input = sys.stdin.readline
MOD = 1000000007


for _ in range(int(input())):
    N = int(input())
    slime = list(map(int, input().split()))
    if N == 1:
        print(1)
        continue


    slime.sort()
    answer = []
    while slime:
        min_val = heappop(slime)
        product = min_val * heappop(slime)

        answer.append(product)
        heappush(slime, product)
        if len(slime) == 1:
            break

    result = 1
    for p in answer:
        result *= p
    print(result % MOD)