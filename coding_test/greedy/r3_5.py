from itertools import combinations


N, M = map(int, input().split())
weight = list(map(int, input().split()))

minus = 0
for i in range(1, M + 1):
    count = weight.count(i)
    if count > 1:
        temp_count = 1
        for j in range(count, 2, -1):
            temp_count *= j
        minus -= temp_count

print(len(list(combinations(weight, 2))) + minus)
