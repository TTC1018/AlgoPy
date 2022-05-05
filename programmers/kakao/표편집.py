def solution(n, k, cmd):
    # 연결 리스트를 표방하는 dictionary
    file = {0: [n - 1, 1]} # 이전 노드는 마지막 노드를 가리킴
    for i in range(1, n - 1):
        file[i] = [i - 1, i + 1]
    file[n - 1] = [n - 2, 0] # 다음 노드는 첫 노드를 가리킴

    removed = []
    cursor = k
    for c in cmd:
        op = c[0]
        if op == 'D': # 내려가기
            for _ in range(int(c.split(' ')[1])):
                cursor = file[cursor][1] # 다음 노드로 이동
        elif op == 'C': # 삭제 후 아래 행 선택
            removed.append((cursor, file[cursor]))
            prev, next = file[cursor]
            file[prev][1], file[next][0] = next, prev
            cursor = file[cursor][0] if file[cursor][1] == 0 else file[cursor][1] # 마지막 노드면 이전 커서 선택
        elif op == 'U': # 올라가기
            for _ in range(int(c.split(' ')[1])):
                cursor = file[cursor][0] # 이전 노드로 이동
        elif op == 'Z': # 최근 삭제 복구
            idx, data = removed.pop()
            prev, next = data
            file[prev][1], file[next][0] = idx, idx # 연결 복구


    answer = ['O'] * n
    for r in removed:
        idx, data = r
        answer[idx] = 'X'
    return ''.join(answer)

print(solution(8, 2,
               ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))