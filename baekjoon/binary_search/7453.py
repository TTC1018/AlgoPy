n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    t_a, t_b, t_c, t_d = map(int, input().split(' '))
    A.append(t_a)
    B.append(t_b)
    C.append(t_c)
    D.append(t_d)


answer = 0
AB = {}
CD = {}
for val_a in A:
    for val_b in B:
        val_ab = val_a + val_b
        AB[val_ab] = AB.get(val_ab, 0) + 1

for val_c in C:
    for val_d in D:
        val_cd = val_c + val_d
        answer += AB.get(-val_cd, 0)

print(answer)