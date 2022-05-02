in_range = lambda x, y: 0 <= x < n and 0 <= y < m
direc = [(-1, -1), (0, -1), (1, -1)]
for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    gold = [data[i*m:(i+1)*m][:] for i in range(n)]
    dp = [[0] * m for _ in range(n)]
    
    # 첫 열 초기화
    for i in range(n):
        dp[i][0] = gold[i][0]
    
    # 지금 위치로 올 수 있는 후보 = 왼쪽위/왼쪽/왼쪽아래
    for col in range(1, m):
        for row in range(n):
            for d in direc:
                nr, nc = row + d[0], col + d[1]
                if in_range(nr, nc):
                    dp[row][col] = max(dp[row][col], dp[nr][nc] + gold[row][col])
    
    # 마지막 열에서 최대값
    print(max([dp[i][m - 1] for i in range(n)]))