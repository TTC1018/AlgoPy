N = int(input())
switch, light = [False] * N, [False] * N

s_ipt = list(map(int, input()))
for i in range(N):
    if s_ipt[i] == 0:
        switch[i] = False
    else:
        switch[i] = True


