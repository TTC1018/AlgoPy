from collections import defaultdict


def solution(id_list, report, k):
    answer = dict()
    for id in id_list:
        answer[id] = 0
    
    # id_list = 전체 유저 목록
    # report = A가 B를 신고했음을 나타내는 신고 문자열들
    # k = 정지 기준이 되는 신고 횟수
    # k에 도달해야 회신 메일을 받을 수 있음
    
    k_dict = defaultdict(list)
    for r in report:
        A, B = r.split(' ')
        if A not in k_dict[B]:
            k_dict[B].append(A)
    
    for id in k_dict:
        count = len(k_dict[id])
        if count >= k:
            for A in k_dict[id]:
                answer[A] += 1
    
    
    answer = list(answer.values())
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))