def dfs(start):
    



N, M = map(int, input().split())
d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

m = []
for _ in range(N):
    m.append(list(map(int, input())))

