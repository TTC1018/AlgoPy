import sys
input = sys.stdin.readline


MOD = 1000000007
def multiply(mat_a, mat_b):
    result = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                result[i][j] += (mat_a[i][k] * mat_b[k][j]) % MOD
            result[i][j] %= MOD
    return result

# 지도를 2차원 배열로 나타내기
# 행렬 곱을 경로의 수로 나타냄
# https://kangminjun.tistory.com/entry/BOJ-12850%EB%B2%88-%EB%B3%B8%EB%8C%80-%EC%82%B0%EC%B1%852
graph = [[0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 1, 1, 0]]
D = int(input())

# 단위행렬
answer = [[0] * 8 for _ in range(8)]
for i in range(8):
    answer[i][i] = 1

while D > 0:
    if D % 2 != 0: # 짝수 아닐 때 축적한 행렬을 갱신해주기
        answer = multiply(answer, graph)
        D -= 1
    graph = multiply(graph, graph) # 거듭제곱 축적
    D //= 2
print(answer[0][0]) # 출발점으로 돌아오는 경우의 수