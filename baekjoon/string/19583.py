import sys
input = sys.stdin.readline


S, E, Q = input().rstrip().split()
s_set, e_set = set(), set()

data = []
while True:
    try:
        data.append(tuple(input().rstrip().split()))
    except EOFError:
        break

nxt = 0
for i in range(len(data)):
    time, name = data[i]
    if time <= S:
        s_set.add(name)
    else:
        nxt = i
        break

for i in range(nxt, len(data)):
    time, name = data[i]
    if E <= time <= Q:
        e_set.add(name)

print(len(s_set.intersection(e_set)))