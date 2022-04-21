import sys
input = sys.stdin.readline


def calc_cost(prv, nxt):
    if prv == nxt:
        return 1
    elif prv == 0:
        return 2
    elif abs(prv - nxt) % 2 == 1:
        return 3
    elif abs(prv - nxt) == 2:
        return 4
    else:
        return INF # 그 이상의 비용 드는 곳은 안 쓰도록 처리
    

INF = int(1e9)
ops = list(map(int, input().split()))
ops.pop() # 마지막은 안 씀
o_len = len(ops)
dp = [[[INF] * 5 for _ in range(5)] for _ in range(o_len + 1)] 
# N번째 단계에서 왼, 오른발이 특정 인덱스에 있을 때 그때까지 소요된 비용을 기록함

dp[0][0][0] = 0
for i in range(1, o_len + 1):
    for left in range(5):
        for right in range(5):
            # 지금 단계에 도달하기 이전에 왼발, 오른발이 left, right에 있는 경우
                        
            if dp[i - 1][left][right] >= INF:
                continue
            nxt = ops[i - 1] # 다음에 눌러야 하는 곳
            l_to_nxt, r_to_nxt = calc_cost(left, nxt), calc_cost(right, nxt) 
            # 왼발로 누르는 경우와 오른발로 누르는 비용 계산
            
            dp[i][nxt][right] = min(dp[i][nxt][right], dp[i - 1][left][right] + l_to_nxt)
            # 왼발을 새로운 곳에 옮긴 경우 = 이전 단계까지 누적된 cost + 새로 들어가는 비용
            
            dp[i][left][nxt] = min(dp[i][left][nxt], dp[i - 1][left][right] + r_to_nxt)
            # 오른발을 새로운 곳에 옮긴 경우 = 이전 단계까지 누적된 cost + 새로 들어가는 비용

answer = INF
for i in range(5):
    answer = min(answer, min(dp[o_len][i]))
print(answer)