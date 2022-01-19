from copy import deepcopy

N = int(input())
have = list(map(int, input().split()))
M = int(input())
search = list(map(int, input().split()))
search_c = deepcopy(search)

search.sort()
d = dict()
for h in have:
    start, end = 0, N - 1
    answer = 0

    if d.get(h):
        d[h] += 1
    else:
        while start <= end:
            mid = (start + end) // 2
            if h < search[mid]:
                end = mid - 1
            elif h > search[mid]:
                start = mid + 1
            else:
                d[h] = 1
                break

for s in search_c:
    if not d.get(s):
        print(0, end = ' ')
    else:
        print(d[s], end = ' ')