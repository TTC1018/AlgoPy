strs = list(input())
target = input()
t_len = len(target)


new_strs = []

for s in strs:
    new_strs.append(s)
    if s == target[-1] and ''.join(new_strs[-t_len:]) == target:
        del new_strs[-t_len:]


if len(new_strs) > 0:
    print(''.join(new_strs))
else:
    print('FRULA')