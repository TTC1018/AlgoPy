from heapq import heappush, heappop
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Counter + heapq
        counter = Counter(nums)
        q = []
        for n in counter:
            heappush(q, (-counter[n], n))

        answer = []
        for _ in range(k):
            answer.append(heappop(q)[1])

        # Only Counter
        answer = list(zip(*Counter(nums).most_common(k)))[0]
        return answer
