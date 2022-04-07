import sys
input = sys.stdin.readline

N = int(input())
nums = sorted((tuple(map(int, input().split())) for _ in range(N))) 
# 튜플 생성이 리스트보다 더 빠름
# 인덱싱도 더 빠르고, 메모리 절약도 됨

# 초기화
answer = nums[0][1] - nums[0][0]
tail = nums[0][1]

for i in range(1, N):
    if nums[i][0] < tail < nums[i][1] or nums[i][0] == tail: # 새 선분이 이전 선분과 겹치거나, 이전 선분 끝점과 새 선분 시작점이 같을 때
        answer += (nums[i][1] - tail) # 이전 선분 끝점부터 새 선분 끝점까지 기록
        tail = nums[i][1] # 가장 우측점 갱신
    elif nums[i][0] > tail: # 새 선분이 이전 선분과 겹치지 않고 우측에 있을 때
        answer += (nums[i][1] - nums[i][0]) # 새 선분 길이 그대로 기록
        tail = nums[i][1] # 가장 우측점 갱신

print(answer)