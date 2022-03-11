from itertools import combinations


N, M = map(int, input().split())
weight = list(map(int, input().split()))

minus = 0
for i in range(1, M + 1):
    count = weight.count(i) # 중복되는 수
    if count > 1: # 2개 이상이면
        temp_count = 1
        for j in range(count, 2, -1):
            temp_count *= j
        minus -= temp_count # combinations(count, 2)값을 minus에 저장

print(len(list(combinations(weight, 2))) + minus) # 전체 조합 수에서 중복 수 조합 빼기