from collections import deque

A, B, C = map(int, input().split())
visited = [[False] * 1501 for _ in range(1501)]
sum_val = A + B + C # 숫자가 변해도 총합은 변하지 않는 다는 것이 핵심

q = deque()
q.append((A, B))
visited[A][B] = True # A와 B라는 두 숫자를 비교했음을 기록

answer = 0
while q:
    a, b = q.popleft()
    c = sum_val - (a + b)

    if a == b == c:
        answer = 1
        break

    for x, y in ((a, b), (b, c), (a, c)):
        if x < y:
            y -= x
            x += x
        elif x > y:
            x -= y
            y += y
        else:
            continue

        z = sum_val - (x + y)

        # 비교할 두 수 고르기
        a = min(min(x, y), z)
        b = max(max(x, y), z)

        # 아직 비교 안 했다면
        if not visited[a][b]:
            q.append((a, b))
            visited[a][b] = True
print(answer)