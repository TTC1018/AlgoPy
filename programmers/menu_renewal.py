from itertools import combinations

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

d = dict()

for o in orders:
    tmp_o = list(o)
    for c_num in course:
        if c_num > len(tmp_o):
            break
        for cand in combinations(tmp_o, c_num):
            cand_str = ''.join(sorted(cand))
            if not d.get(cand_str):
                d[cand_str] = 1
            else:
                d[cand_str] += 1

a_dict = dict()    
for k, v in d.items():
    t_num = len(k)
    if not a_dict.get(t_num):
        if v > 1:
            a_dict[t_num] = ([k], v)
    else:
        if a_dict[t_num][1] < v:
            a_dict[t_num] = ([k], v)
        elif a_dict[t_num][1] == v:
            a_dict[t_num][0].append(k)

answer = []
for c_num in course:
    if a_dict.get(c_num):
        for t_ans in a_dict[c_num][0]:
            answer.append(t_ans)
answer.sort()
print(answer)