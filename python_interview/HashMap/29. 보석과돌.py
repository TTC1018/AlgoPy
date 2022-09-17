from collections import defaultdict, Counter
import re


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0

        # 정규식 풀이
        r_str = f'[{jewels}]'
        regex = re.compile(r_str)

        for s in stones:
            if regex.match(s):
                answer += 1

        # dict 풀이
        d = defaultdict(int)
        for s in stones:
            d[s] += 1

        for key in d:
            if key in jewels:
                answer += d[key]

        # Counter 풀이
        counter = Counter(stones)
        for j in jewels:
            answer += counter[j] # 없으면 0 return

        # 리스트 내포
        answer = sum(s in jewels for s in stones)

        return answer