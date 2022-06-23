import sys
input = sys.stdin.readline

N, K = map(int, input().split())
H = list(map(int, input().split()))
print(sum(sorted([H[i + 1] - H[i] for i in range(N - 1)])[:N-K]))
# 원생 간의 거리를 더하는 행위 = 같은 조로 흡수하거나 새로운 조를 만드는 것
