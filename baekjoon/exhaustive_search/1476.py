nums = input().split(' ')
E = int(nums[0])  # 1..15
S = int(nums[1])  # 1..28
M = int(nums[2])  # 1..19

year = 0
TE = 0
TS = 0
TM = 0

while True:
    TE += 1
    if TE == 16:
        TE = 1
    TS += 1
    if TS == 29:
        TS = 1
    TM += 1
    if TM == 20:
        TM = 1
    year += 1
    if TE == E and TS == S and TM == M:
        break

print(year)