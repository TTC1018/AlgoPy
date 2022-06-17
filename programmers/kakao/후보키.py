from itertools import combinations


def solution(relation):
    answer = set()
    total = len(relation)
    attr = [i for i in range(len(relation[0]))]
    
    for n in range(1, len(attr) + 1):
        for c in combinations(attr, n):
            tuples = set()
            for i in range(total):
                tuples.add(tuple([relation[i][a] for a in c]))
            if len(tuples) == total:
                sc = set(c)
                for a in answer:
                    if set(a) <= sc:
                        break
                else:
                    answer.add(c)
    return len(answer)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
                ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))