def solution(food_times, k):

    answer = 0
    sec, f_len = 0, len(food_times)
    for i in range(f_len):
        food_times[i] *= f_len

    while f_len > 0:
        mf_time = min(food_times)
        if mf_time > k:
            answer = k % f_len
            break
        else:
            k -= mf_time
            food_times.pop(food_times.index(min(food_times)))
            f_len -= 1
            for i in range(f_len):
                food_times[i] -= mf_time

    if f_len == 0:
        answer = -2
    return answer + 1

print(solution([3,1,2], 5))