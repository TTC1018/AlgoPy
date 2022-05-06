def calc_dist(x, y, tx ,ty):
    return abs(x - tx) + abs(y - ty)


def solution(numbers, hand):
    answer = ''
    
    num_pos = []
    for n in numbers:
        if n == 0:
            num_pos.append((3, 1))
        else:
            div, mod = divmod(n - 1, 3)
            num_pos.append((div, mod))
    
    lx, ly = 3, 0 # 왼손 좌표
    rx, ry = 3, 2 # 오른손 좌표   
    
    n_len = len(numbers) 
    for i in range(n_len):
        x, y = num_pos[i]
        if numbers[i] in [1, 4, 7]:
            lx, ly = x, y
            answer += 'L'
        elif numbers[i] in [3, 6, 9]:
            rx, ry = x, y
            answer += 'R'
        else: # 중앙 라인
            l_dist = calc_dist(x, y, lx, ly)
            r_dist = calc_dist(x, y, rx, ry)
            if l_dist == r_dist: # 거리 같으면
                if hand == 'left': # 왼손잡이
                    answer += 'L'
                    lx, ly = x, y
                else:
                    answer += 'R'
                    rx, ry = x, y
            elif l_dist < r_dist:
                answer += 'L'
                lx, ly = x, y
            elif r_dist < l_dist:
                answer += 'R'
                rx, ry = x, y
                

    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))