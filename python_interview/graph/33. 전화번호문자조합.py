from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(now, stacked):
            if len(stacked) == len(digits):
                answer.append(stacked)
                return

            for i in range(now, len(digits)):
                for nxt in d[digits[i]]:
                    dfs(i + 1, stacked + nxt)

        if not digits:
            return []

        digits = list(map(int, list(digits)))
        combs = set()

        d = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
             5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
             8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

        answer = []
        dfs(0, "")
        return answer