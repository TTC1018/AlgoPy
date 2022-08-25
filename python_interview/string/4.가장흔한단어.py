import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # paragraph = re.sub('[!?,;.\']', ' ', paragraph).lower().split()
        # counter = Counter(paragraph).most_common()
        # banned = set(banned)
        # for word, count in counter:
        #     if word not in banned:
        #         return word

        # 교재 해답
        banned = set(banned)
        paragraph = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split()
                     if word not in banned]
        return Counter(paragraph).most_common(1)[0][0]