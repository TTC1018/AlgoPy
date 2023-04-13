import sys
input = sys.stdin.readline
INF = int(1e9)


N, M = map(int, input().split())
edge = [[-1] * N for _ in range(N)]
dist = [[INF] * N for _ in range(N)]
for _ in range(M):
    S, E, L = map(int, input().split())
    S -= 1; E -= 1

    # 가장 긴 간선 남기기
    if edge[S][E] < L: edge[S][E] = L
    if edge[E][S] < L: edge[E][S] = L

    # 가장 짧은 간선 남기기
    if dist[S][E] > L: dist[S][E] = L
    if dist[E][S] > L: dist[E][S] = L
for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


answer = INF
for s in range(N):
    longest = 0

    for f in range(N):
        for t in range(N):
            e = edge[f][t]
            if e != -1: # f - t 연결돼있을 때
                remain = e - (dist[s][t] - dist[s][f]) # 남은 길이 = f -> t로 가기전에 s -> t, s -> f에 걸린 시간 제거
                if remain > 0:
                    longest = max(longest, remain / 2 + dist[s][t]) # f <-> t 양쪽으로 타기 때문에 나누기 2

    answer = min(answer, longest)
print(answer)