from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        limit = len(nums)
        def dfs(idx, stacked):
            answer.append(stacked)

            for i in range(idx, limit):
                dfs(i + 1, stacked + [nums[i]])


        dfs(0, [])
        return answer