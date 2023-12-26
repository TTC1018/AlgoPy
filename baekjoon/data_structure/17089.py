import sys
input = sys.stdin.readline
INF = int(1e9)
# 세 사람의 친구의 수 구하기
# 합이 최소가 되도록 선택
# 세 사람이 모두 친구여야 됨
# 어차피 세 사람이 모두 친구이므로, 답에서 6을 빼야됨

N, M = map(int, input().split())
F = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    F[a].add(b)
    F[b].add(a)

# 두명을 고르고 교집합을 찾는다.
answer = INF
visited = set()
for a in range(N):
    for b in range(a + 1, N):
        if a != b and b in F[a] and a in F[b]:
            for c in F[a].intersection(F[b]):
                v = tuple(sorted((a, b, c)))
                if v not in visited:
                    visited.add(v)
                    answer = min(answer, len(F[a]) + len(F[b]) + len(F[c]) - 6)
if answer == INF:
    print(-1)
else:
    print(answer)