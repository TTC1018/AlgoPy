import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()

psum = P[:]
for i in range(N - 1):
    psum[i + 1] += psum[i]
print(sum(psum))
