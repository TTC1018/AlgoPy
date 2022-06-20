from itertools import combinations


def solution(relation):
    answer = set()
    total = len(relation) # 데이터 개수
    attr = [i for i in range(len(relation[0]))] # 속성들을 인덱스로 저장
    
    for n in range(1, len(attr) + 1): # 속성 몇개를 고를 것인지
        for c in combinations(attr, n): # 조합으로 속성 n개 고르기
            tuples = set()
            for i in range(total): # 각 데이터에서 속성 n개만 추려내기
                tuples.add(tuple([relation[i][a] for a in c]))
            if len(tuples) == total: # 유일성 만족한다면
                sc = set(c)
                for a in answer: # 이전 후보키를 포함하는지 확인
                    if set(a) <= sc: # 포함하면 최소성 만족 못 함
                        break
                else: # 포함 안 하면 새로운 후보키
                    answer.add(c)
    return len(answer)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
                ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))