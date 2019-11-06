import score

EXTEND = 1
OPENGAP = 11

file = open('BLOSUM62.txt')
file = file.read().split('\n')
keys = file[0].split()
BLOSUM62 = {}
for i in range(1, len(file)):
    temp = file[i].split()
    key2 = temp[0]
    for j, key in enumerate(keys):
        if not key in BLOSUM62:
            BLOSUM62[key] = {key2: int(temp[j + 1])}
        else:
            BLOSUM62[key][key2] = int(temp[j + 1])

def GlobalAlignment(v, w):
    v = '-' + v
    w = '-' + w

    ## Initialize Score Matrices
    Middle = [[0 for i in range(len(w))] for j in range(len(v))]
    Lower = [[0 for i in range(len(w))] for j in range(len(v))]
    Upper = [[0 for i in range(len(w))] for j in range(len(v))]

    Middle[1][0] = - OPENGAP
    Middle[0][1] = - OPENGAP
    for i in range(2, len(Middle)):
        Middle[i][0] = Middle[i - 1][0] - EXTEND
    for j in range(2, len(Middle[0])):
        Middle[0][j] = Middle[0][j - 1] - EXTEND

    for j in range(len(Lower[0])):
        Lower[0][j] = -1e6
    for i in range(0, len(Lower)):
        Lower[i][0] = Middle[i][0]
    for i in range(len(Upper)):
        Upper[i][0] = -1e6
    for j in range(0, len(Upper[0])):
        Upper[0][j] = Middle[0][j]

    ## Initialize Backtrack Matrices
    BacktrackM = [[4 for i in range(len(w))] for j in range(len(v))]
    BacktrackL = [[2 for i in range(len(w))] for j in range(len(v))]
    BacktrackU = [[1 for i in range(len(w))] for j in range(len(v))]
    
    for i in range(len(BacktrackM)):
        BacktrackM[i][0] = 2
    for j in range(len(BacktrackM[0])):
        BacktrackM[0][j] = 1

    for j in range(len(BacktrackL[0])):
        BacktrackL[0][j] = 1
    for i in range(len(BacktrackU)):
        BacktrackU[i][0] = 2

    BacktrackM[0][0] = 0
    BacktrackL[0][0] = 0
    BacktrackU[0][0] = 0

    ## DP
    for i in range(1, len(v)):
        for j in range(1, len(w)):

            Lower[i][j] = max(Lower[i - 1][j] - EXTEND, Middle[i - 1][j] - OPENGAP)
            if Lower[i][j] == Lower[i - 1][j] - EXTEND:
                BacktrackL[i][j] = 2
            else:
                BacktrackL[i][j] = 4

            Upper[i][j] = max(Upper[i][j -1] - EXTEND, Middle[i][j - 1] - OPENGAP)
            if Upper[i][j] == Upper[i][j -1] - EXTEND:
                BacktrackU[i][j] = 1
            else:
                BacktrackU[i][j] = 4

            diag = Middle[i - 1][j - 1] + BLOSUM62[v[i]][w[j]]
            
            Middle[i][j] = max([diag, Upper[i][j], Lower[i][j]])

            if Middle[i][j] == diag:
                BacktrackM[i][j] = 4
            elif Middle[i][j] == Lower[i][j]:
                BacktrackM[i][j] = 2
            else:
                BacktrackM[i][j] = 1

    # # Debugging
    # for row in Middle:
    #     print(' '.join(map(str, row)))
    # print("################ Upper ################")
    # for row in Upper:
    #     print(' '.join(map(str, row)))
    # print("################ Lower ################")
    # for row in Lower:
    #     print(' '.join(map(str, row)))

    # file = open('Scores.txt', 'w') 
    # file.write("################ Middle ################\n")
    # for row in Middle:
    #     file.write(' '.join(map(str, row)) + '\n')
    # file.write("################ Lower ################\n")
    # for row in Lower:
    #     file.write(' '.join(map(str, row)) + '\n')
    # file.write("################ Upper ################\n")
    # for row in Upper:
    #     file.write(' '.join(map(str, row)) + '\n')
    # file.close()
    # file = open('Backtracks.txt', 'w') 
    # file.write("################ Middle ################\n")
    # for row in BacktrackM:
    #     file.write(' '.join(map(str, row)) + '\n')
    # file.write("################ Lower ################\n")
    # for row in BacktrackL:
    #     file.write(' '.join(map(str, row)) + '\n')
    # file.write("################ Upper ################\n")
    # for row in BacktrackU:
    #     file.write(' '.join(map(str, row)) + '\n')
    # file.close()
    # print("################ Middle ################")
    # for row in BacktrackM:
    #     print(' '.join(map(str, row)))
    # print("################ Lower ################")
    # for row in BacktrackL:
    #     print(' '.join(map(str, row)))
    # print("################ Upper ################")
    # for row in BacktrackU:
    #     print(' '.join(map(str, row)))
    # print(' ')

    print(Middle[len(v) - 1][len(w) - 1])
    return (BacktrackM, BacktrackL, BacktrackU)

def Alignment(BacktrackM, BacktrackL, BacktrackU, v, w):
    i = len(BacktrackM) - 1
    j = len(BacktrackM[0]) - 1
    res_v = ''
    res_w = ''
    current = 'M'
    while BacktrackM[i][j] != 0:
        if current == 'M':
            if BacktrackM[i][j] == 4:
                res_v = v[i - 1] + res_v
                res_w = w[j - 1] + res_w
                i -= 1
                j -= 1
            elif BacktrackM[i][j] == 2:
                current = 'L'
            else:
                current = 'U'

        elif current == 'L':
            if BacktrackL[i][j] == 2:
                res_v = v[i - 1] + res_v
                res_w = '-' + res_w
                i -= 1
            elif BacktrackL[i][j] == 4:
                res_v = v[i - 1] + res_v
                res_w = '-' + res_w
                i -= 1
                current = 'M'
            else:
                current = 'M'

        elif current == 'U':
            if BacktrackU[i][j] == 1:
                res_v = '-' + res_v
                res_w = w[j - 1] + res_w
                j -= 1
            elif BacktrackL[i][j] == 4:
                res_v = '-' + res_v
                res_w = w[j - 1] + res_w
                j -= 1
                current = 'M'
            else:
                current = 'M'
                
    print(res_v)
    print(res_w)
    return (res_v, res_w)

if __name__ == "__main__":
    v = input().rstrip()
    w = input().rstrip()
    BacktrackM, BacktrackL, BacktrackU = GlobalAlignment(v, w)
    # for row in Backtrack:
    #     print(' '.join(map(str, row)))
    res_v, res_w = Alignment(BacktrackM, BacktrackL, BacktrackU, v, w)
    print(score.Score(res_v, res_w))