from collections import deque

F, S, G, U, D = list(map(int, input().split(' ')))

visited = [0] * (F+1)
visited[S] = 1

answer = F
flag = False

q = deque()
q.append((S, 0))
while q:
    now, count = q.popleft()
    if now == G:
        if answer > count:
            answer = count
            flag = True
        continue

    next_up = now + U if now + U <= F else now
    next_down = now - D if now - D >= 1 else now

    if visited[next_up] == 0:
        visited[next_up] += 1
        q.append((next_up, count + 1))
    if visited[next_down] == 0:
        visited[next_down] += 1
        q.append((next_down, count + 1))

if flag:
    print(answer)
else:
    print('use the stairs')