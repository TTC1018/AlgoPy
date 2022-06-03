import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(num):
    global answer, K
    if graph[num] == (-1, -1):
        answer = num
        return

    left, right = graph[num]
    if right == -1:
        dfs(left)
    elif left == -1:
        dfs(right)
    elif (left, right) != (-1, -1):
        if K % 2 == 1: # 홀수번째 차례인 경우, 좌로 떨어짐
            K = K // 2 + 1
            dfs(left)
        else: # 짝수번째 차례인 경우, 우로 떨어짐
            K //= 2
            dfs(right)


N = int(input())
graph = [-1] + [tuple(map(int, input().split())) for _ in range(N)]
K = int(input())

answer = 0
dfs(1) # 홀수/짝수번째 차례에 따라 방향이 정해진다는 규칙에 입거하여 한번만 탐색해도 됨
print(answer)