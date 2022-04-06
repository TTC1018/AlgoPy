def count_parent(num):
    count = 0
    count += len(parents[num])
    for next in parents[num]:
        count += count_parent(next)
    return count


def dynamic(num):
    for next in parents[num]:
            dp[next] = max(dp[next], dp[num] + D[next])
            dynamic(next)


INF = int(1e9)
for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [-1] + list(map(int, input().split()))
    
    parents = [[] for _ in range(N + 1)]
    for i in range(K):
        X, Y = map(int, input().split())
        parents[X].append(Y)
        
    W = int(input())
    
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = D[i]
    
    start = 1
    count = 0
    for i in range(1, N + 1):
        temp_count = count_parent(i)
        if count < temp_count:
            count = temp_count
            start = i
    
    dynamic(start)
    print(dp[W])