def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 2):
        prev = s[:i]
        counter = 1
        t_answer = ''
        for j in range(i, len(s) + i, i):
            if prev == s[j:j+i]:
                counter += 1
            else:
                if counter == 1:
                    t_answer += prev
                else:
                    t_answer += (str(counter) + prev)
                prev = s[j:j+i]
                counter = 1
        
        answer = min(answer, len(t_answer))
    
    return answer

print(solution('aabbaccc'))