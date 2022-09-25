from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(stacked, start, rest):
            if rest == 0:
                answer.append(stacked[:])
                return

            for i in range(start, n + 1):
                stacked.append(i)
                dfs(stacked, i + 1, k - 1)
                stacked.pop()

        answer = []
        dfs([], 1, k)
        return answer

        return combinations([num for num in range(1, n + 1)], k)