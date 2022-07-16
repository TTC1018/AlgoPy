from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)

        # for string in strs:
        #     counter = Counter(string)
        #     d[tuple(sorted([key + str(counter[key]) for key in counter]))].append(string)
        # return d.values()

        # 해답
        for word in strs:
            d[''.join(sorted(word))].append(word)
        return d.values()