def solution(files):

    file_split = [] # HEAD, NUMBER, TAIL 끊어서 저장할 리스트
    for f in files:
        f_len = len(f)
        tmp = []
        # HEAD 처리
        for i in range(f_len):
            if f[i].isnumeric(): # HEAD 끝나는 지점 (숫자)
                tmp.append(f[:i]) # HEAD 저장
                # NUMBER 처리
                limit = min(i + 5, f_len) # 5자리 글자 전에 문자열 끝나는 거 방지
                for j in range(i, limit):
                    if not f[j].isnumeric(): # NUMBER 끝나는 지점
                        tmp.append(f[i:j])
                        tmp.append(f[j:]) # TAIL
                        break
                else:
                    tmp.append(f[i:limit])
                    if limit < f_len:
                        tmp.append(f[limit:]) # TAIL
                    else:
                        tmp.append('')
                break
        file_split.append(tmp)

    file_split.sort(key=lambda x:(x[0].lower(), int(x[1])))
    answer = [''.join(x) for x in file_split] # 다시 합쳐주기

    return answer

# 모범 답안
# import re
#
# def solution(files):
#     a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0])) # NUMBER 비교
#     b = sorted(a, key=lambda file : re.split('\d{1,5}', file.lower())[0]) #HEAD 비교
#     return b


print(solution(["F-15"]))