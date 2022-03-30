N, M = map(int, input().split())
locs = list(map(int, input().split()))
locs.sort()

loc_m = [i for i in locs if i < 0]
loc_p = [i for i in locs if i > 0]

answer = 0
m_last, p_last = 0, 0
while loc_m:
    if len(loc_m) > M:
        answer += (abs(loc_m[0]) * 2)
        for _ in range(M):
            loc_m.pop(0)
    else:
        start, end = loc_m[0], loc_m[-1]
        answer += (abs(start) + abs(start - end))
        m_last = abs(loc_m[-1])
        break
while loc_p:
    if len(loc_p) > M:
        answer += (abs(loc_p[-1]) * 2)
        for _ in range(M):
            loc_p.pop()
    else:
        start, end = loc_p[-1], loc_p[0]
        answer += (start + (start - end))
        p_last = end
        break

answer += min(m_last, p_last)
print(answer)