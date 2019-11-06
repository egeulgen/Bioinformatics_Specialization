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
    S = [[0 for i in range(len(w))] for j in range(len(v))]
    Backtrack = [[0 for i in range(len(w))] for j in range(len(v))]
    for i in range(1, len(S)):
        S[i][0] = S[i - 1][0] - 5
        Backtrack[i][0] = 1
    for j in range(1, len(S[0])):
        S[0][j] = S[0][j - 1] - 5
        Backtrack[0][j] = 2
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            diag = S[i - 1][j - 1] + BLOSUM62[v[i]][w[j]]
            down = S[i - 1][j] - 5
            right = S[i][j - 1] - 5
            S[i][j] = max([down, right, diag])
            if S[i][j] == down:
                Backtrack[i][j] = 1
            elif S[i][j] == right:
                Backtrack[i][j] = 2
            else:
                Backtrack[i][j] = 4
    for row in S:
        print(' '.join(map(str, row)))
    print(S[len(v) - 1][len(w) - 1])
    return Backtrack

def Alignment(Backtrack, v, w):
    i = len(Backtrack) - 1
    j = len(Backtrack[0]) - 1
    res_v = ''
    res_w = ''
    while i > 0 or j > 0:
        if Backtrack[i][j] == 4:
            res_v = v[i - 1] + res_v
            res_w = w[j - 1] + res_w
            i -= 1
            j -= 1
        elif Backtrack[i][j] == 2:
            res_v = '-' + res_v
            res_w = w[j - 1] + res_w
            j -= 1
        else:
            res_v = v[i - 1] + res_v
            res_w = '-' + res_w
            i -= 1
    print(res_v)
    print(res_w)


if __name__ == "__main__":
    v = 'PLEASANTLY'
    w = 'MEANLY'
    Backtrack = GlobalAlignment(v, w)
    Alignment(Backtrack, v, w)