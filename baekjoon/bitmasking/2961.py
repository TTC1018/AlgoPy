import sys
input = sys.stdin.readline


N = int(input())
material = []
for _ in range(N):
    S, B = map(int, input().split())
    material.append((S, B))
    # 신맛은 곱, 쓴맛은 합
    # 신맛과 쓴맛의 차이 최소로

answer = int(1e9)
for case in range(1, 1 << N):
    sour, bitter = 1, 0
    for i in range(N):
        bit = 1 << i
        if case & bit:
            sour *= material[i][0]
            bitter += material[i][1]
    answer = min(answer, abs(sour - bitter))
print(answer)