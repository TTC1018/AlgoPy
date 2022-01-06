rc = input()
r = int(rc[1])
c = ord(rc[0]) - 96 # a 아스키코드 97

f_dir = [(-2, 0), (2, 0), (0, -2), (0, 2)]

answer = 0
for d in f_dir:
    fx, fy = d[0], d[1]
    if fx == 0:
        for nx in [fx - 1, fx + 1]:
            if 1 <= nx <= 8 and 1 <= fy <= 8:
                answer += 1
    else:
        for ny in [fy-1, fy+1]:
            if 1 <= fx <= 8 and 1 <= ny <= 8:
                answer += 1
print(answer)