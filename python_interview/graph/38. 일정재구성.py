from collections import defaultdict, deque
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(now):
            while nxt_dst[now]:
                dfs(nxt_dst[now].popleft())
            answer.appendleft(now)

        nxt_dst = defaultdict(deque)
        for f, t in sorted(tickets):
            nxt_dst[f].append(t)

        start = 'JFK'
        answer = deque()
        dfs(start)
        return list(answer)