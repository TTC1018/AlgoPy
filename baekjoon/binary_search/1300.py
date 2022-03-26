N = int(input())
k = int(input())
#  1 2 3
#1 1 2 3 3
#2 2 4 6 2
#3 3 6 9 1

# 1 2 3 4 5 6 7 8 9
# 1 2 2 3 3 4 6 6 9
# 행번호로 나눴을 때의 몫 = 해당 행에 존재하는 대상숫자 이하의 수
start, end = 1, k
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    
    for i in range(1, N + 1):
        if mid // i == 0:
            break
        else:
            cnt += min(mid // i, N)
    
    if cnt >= k:
        end = mid - 1
    else:
        start = mid + 1
print(start)