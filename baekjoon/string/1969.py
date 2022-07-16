from collections import defaultdict
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
DNA = [input().rstrip() for _ in range(N)]

answer = ''
distance = 0
for j in range(M):
    d = defaultdict(int)
    for i in range(N):
        d[DNA[i][j]] += 1

    d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    answer += d[0][0]
    distance += (N - d[0][1])
print(answer, distance, sep='\n')
