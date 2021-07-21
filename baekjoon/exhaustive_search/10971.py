def solve(prev, dest, cost, W, visited, N):
    global answer

    if len(visited) == N and W[dest][prev] != 0:
        if W[dest][prev] != 0:
            answer = min(answer, cost + W[dest][prev])
        return

    for i in range(N):
        if W[dest][i] != 0 and i != prev and i not in visited:
            visited.append(i)
            if answer > cost + W[dest][i]:
                solve(prev, i, cost + W[dest][i], W, visited, N)
                visited.pop()
            else:
                visited.pop()
                continue


N = int(input())
W = [list(map(int, input().split(' '))) for _ in range(N)]

answer = 1000000*N
for i in range(N):
    solve(i, i, 0, W, [i], N)

print(answer)