from itertools import combinations
from collections import deque

N, K = map(int, input().split())
M = len(str(N))
case = list(combinations([i for i in range(M)], 2))

visited = set()
q = deque()
q.append(N)
answer = 0
while q:
    num = q.popleft()
    num_list = list(str(num))
    for i, j in case:
        num_cpy = num_list[:]
        num_cpy[i], num_cpy[j] = num_cpy[j], num_cpy[i]
        if num_cpy[0] != '0': # 첫자리 0 아니면
            generated = int(''.join(num_cpy))
            if generated not in visited:
                visited.add(generated)
                q.append(generated) 

if not answer:
    print(-1)
else:
    print(answer)