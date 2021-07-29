from collections import deque

target = 123456789
P = []
for i in range(3):
    P.append(''.join([n for n in input().split(' ')]))
P = int(''.join(P).replace('0', '9'))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dist = dict()

answer = -1
q = deque()
q.append(P)
dist[P] = 0
while q:
    temp = q.popleft()

    if temp == target:
        answer = dist[temp]
        break

    temp_str = str(temp)
    z = temp_str.find('9')
    a, b = z // 3, z % 3

    for i in range(4):
        new_a = a + dx[i]
        new_b = b + dy[i]
        if 0 <= new_a <= 2 and 0 <= new_b <= 2:
            new_z = new_a * 3 + new_b
            temp_list = list(temp_str)
            temp_list[new_z], temp_list[z] = temp_list[z], temp_list[new_z]

            new_temp = int(''.join(temp_list))
            if not dist.get(new_temp):
                dist[new_temp] = dist[temp] + 1
                q.append(new_temp)

print(answer)