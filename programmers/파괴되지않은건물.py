from collections import defaultdict

b_graph = []
# def attack(start, end, degree):
#     global b_graph
#     for i in range(start[0], end[0] + 1):
#         for j in range(start[1], end[1] + 1):
#             b_graph[i][j] -= degree


# def heal(start, end, degree):
#     global b_graph
#     for i in range(start[0], end[0] + 1):
#         for j in range(start[1], end[1] + 1):
#             b_graph[i][j] += degree


def unbroken():
    global b_graph
    r_len = len(b_graph)
    c_len = len(b_graph[0])
    
    b_cnt = 0
    for i in range(r_len):
        for j in range(c_len):
            if b_graph[i][j] > 0:
                b_cnt += 1
    return b_cnt
                
            
def solution(board, skill):
    # global b_graph
    answer = 0
    # b_graph = board
    # skill = [type, r1, c1, r2, c2, degree]
    # type = 1 (공격) or 2 (회복)
    
    damage = defaultdict(int)
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        if type == 1: # 공격
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    damage[(i, j)] -= degree
            # attack((r1, c1), (r2, c2), degree)
        elif type == 2: # 회복
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    damage[(i, j)] += degree
            # heal((r1, c1), (r2, c2), degree)
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + damage[(i, j)] > 0:
                answer += 1

    return answer