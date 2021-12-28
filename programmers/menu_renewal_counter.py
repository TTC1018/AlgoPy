from collections import Counter
from itertools import combinations

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

answer = []
for c_num in course:
    o_coms = []
    for o in orders:
        o_coms.extend(combinations(sorted(o), c_num))

    c_list = Counter(o_coms).most_common()
    answer.extend([''.join(k) for k, v in c_list if v > 1 and v == c_list[0][1]])
answer.sort()
print(answer)