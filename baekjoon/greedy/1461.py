N, M = map(int, input().split())
locs = list(map(int, input().split()))
locs.sort()

loc_m = [i for i in locs if i < 0]
loc_p = [i for i in locs if i > 0]

targets = []
while loc_m:
    if len(loc_m) > M:
        temp_t = []
        for i in range(M):
            temp_t.append(loc_m.pop(0))
        targets.append(temp_t)
    else:
        targets.append(loc_m)
        break
while loc_p:
    if len(loc_p) > M:
        temp_t = []
        for i in range(M):
            temp_t.append(loc_p.pop())
        targets.append(temp_t)
    else:
        loc_p.reverse()
        targets.append(loc_p)
        break

targets.sort()
answer = 0
for t in targets:
    answer += (abs(t[0]) * 2)
answer -= max(abs(targets[0][0]), abs(targets[-1][0]))
print(answer)