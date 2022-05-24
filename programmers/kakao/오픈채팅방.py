def solution(record):
    answer = []

    nick_dict = dict()
    log = []
    for r in record:
        data = r.split()
        if data[0] == 'Enter' or data[0] == 'Change':
            nick_dict[data[1]] = data[2]
        if data[0] == 'Enter' or data[0] == 'Leave':
            log.append((data[0], data[1]))

    for l in log:
        op, id = l
        if op == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(nick_dict[id]))
        else:
            answer.append('{}님이 나갔습니다.'.format(nick_dict[id]))

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))