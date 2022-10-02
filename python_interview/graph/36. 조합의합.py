from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(now_idx, stacked, sum_val):
            if sum_val == target:
                answer.append(stacked)

            for i in range(now_idx, limit):
                if sum_val + candidates[i] <= target:
                    dfs(i, stacked + [candidates[i]], sum_val + candidates[i])

        limit = len(candidates)
        for i in range(limit):
            dfs(i, [candidates[i]], candidates[i])

        return answer