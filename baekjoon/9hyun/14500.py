import sys
input = sys.stdin.readline


def long():
    sum_val = 0
    # ####
    for i in range(N): # 행
        for j in range(M - 3): # 열
            sum_val = max(sum_val, sum(paper[i][j:j+4]))
    
    #   #
    #   #
    #   #
    #   #
    for i in range(M): # 열
        for j in range(N - 3): # 행
            sum_val = max(sum_val, sum([paper[row][i] for row in range(j, j + 4)]))    
    return sum_val


def square():
    sum_val = 0
    for i in range(N - 1):
        for j in range(M - 1):
            sum_val = max(sum_val, sum(paper[i][j:j+2]) + sum(paper[i + 1][j:j+2]))
    return sum_val


def lightning():
    sum_val = 0

    #   #
    #   ##
    #    #
    for i in range(N - 2):
        for j in range(M - 1):
            sum_val = max(sum_val, sum([paper[i][j], paper[i + 1][j],
                                       paper[i + 1][j + 1], paper[i + 2][j + 1]]))

    #    ##
    #   ##
    for i in range(1, N):
        for j in range(M - 2):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                       paper[i - 1][j + 1], paper[i - 1][j + 2]]))

    #   ##
    #    ##
    for i in range(N - 1):
        for j in range(M - 2):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                        paper[i + 1][j + 1], paper[i + 1][j + 2]]))

    #    #
    #   ##
    #   #
    for i in range(1, N - 1):
        for j in range(M - 1):
            sum_val = max(sum_val, sum([paper[i][j], paper[i + 1][j],
                                       paper[i][j + 1], paper[i - 1][j + 1]]))

    return sum_val


def middle():
    sum_val = 0
    
    #  #
    # ###
    for i in range(1, N):
        for j in range(M - 2):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                       paper[i - 1][j + 1], paper[i][j + 2]]))
    #   ###
    #    #
    for i in range(N - 1):
        for j in range(M - 2):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                       paper[i + 1][j + 1], paper[i][j + 2]]))
    #   #
    #   ##
    #   #
    for i in range(N - 2):
        for j in range(M - 1):
            sum_val = max(sum_val, sum([paper[i][j], paper[i + 1][j],
                                       paper[i + 1][j + 1], paper[i + 2][j]]))
    #    #
    #   ##
    #    #
    for i in range(1, N - 1):
        for j in range(M - 1):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                    paper[i - 1][j + 1], paper[i + 1][j + 1]]))
    
    return sum_val


def nieun():
    sum_val = 0
    #
    #
    ##
    for i in range(N - 2):
        for j in range(M - 1):
            sum_val = max(sum_val, sum([paper[i][j], paper[i + 1][j],
                                       paper[i + 2][j], paper[i + 2][j + 1]]))
    ##
     #
     #
    for i in range(N - 2):
        for j in range(M - 1):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                       paper[i + 1][j + 1], paper[i + 2][j + 1]]))
      #
    ###
    for i in range(1, N - 1):
        for j in range(M - 2):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                       paper[i][j + 2], paper[i - 1][j + 2]]))
    ###
    #
    for i in range(N - 1):
        for j in range(M - 2):
            sum_val = max(sum_val, sum([paper[i][j], paper[i + 1][j],
                                       paper[i][j + 1], paper[i][j + 2]]))

     #
     #
    ##
    for i in range(2, N):
        for j in range(M - 1):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                       paper[i - 1][j + 1], paper[i - 2][j + 1]]))

    ##
    #
    #
    for i in range(N - 2):
        for j in range(M - 1):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                       paper[i + 1][j], paper[i + 2][j]]))

    #
    ###
    for i in range(N - 1):
        for j in range(M - 2):
            sum_val = max(sum_val, sum([paper[i][j], paper[i + 1][j],
                                        paper[i + 1][j + 1], paper[i + 1][j + 2]]))

    ###
      #
    for i in range(N - 1):
        for j in range(M - 2):
            sum_val = max(sum_val, sum([paper[i][j], paper[i][j + 1],
                                        paper[i][j + 2], paper[i + 1][j + 2]]))

    return sum_val

    
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
print(max(long(), square(), middle(), nieun(), lightning()))