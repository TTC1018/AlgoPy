from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # DFS
        def dfs(ns):
            if len(ns) == 0:
                answer.append(per[:])
                return

            for n in ns:
                per.append(n)
                dfs([num for num in ns if num != n])
                per.remove(n)

        answer = []
        per = []
        dfs(nums)
        return answer


        # 라이브러리로 풀기
        return permutations(nums, len(nums))