import heapq


def solution(food_times, k):
    answer = -1

    q = []
    f_len = len(food_times)
    for i in range(f_len):
        heapq.heappush(q, (food_times[i], i + 1)) # 가장 빨리 소모될 수 있는 음식 순서로 삽입

    previous = 0
    while q:
        temp_time = (q[0][0] - previous) * f_len # 현재 최소의 양을 가지는 음식이 소요되는 시간
        if temp_time <= k: # k초 이내에 소모 되는 경우
            k -= temp_time
            previous = heapq.heappop(q)[0] # 다음 루프에서 사용하기 위해 기록함
            f_len -= 1
        else: # k초 이내에 소모 불가한 경우 (끝내야 되는 경우)
            idx = k % f_len
            q.sort(key=lambda x: x[1]) # 다시 인덱스 순서로 정렬
            answer = q[idx][1]
            break

    return answer


print(solution([3, 2, 2], 5))
