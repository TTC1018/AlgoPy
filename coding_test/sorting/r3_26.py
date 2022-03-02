import heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

answer = 0
while len(cards) != 1:
    temp_sum = (heapq.heappop(cards) + heapq.heappop(cards))
    answer += temp_sum
    heapq.heappush(cards, temp_sum)
print(answer)


# 단순 오름차순 정렬 후에 하나씩 더하는 것에는 반례가 있음
# 15 15 15 20 일 때,
# 단순 오름차순 정렬 계산은
# (15 + 15) + (15 + 15 + 15) + (15 + 15 + 15 + 20) = 140
# 그러나 heapq 사용 시에는 (15 + 15) + (15 + 20) + (15 + 15 + 15 + 20) = 130