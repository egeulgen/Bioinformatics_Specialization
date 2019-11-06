import sys
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

def TripleAlignment(v, w, u):
    v = '-' + v
    w = '-' + w
    u = '-' + u
    S = [[[0 for i in range(len(u))] for j in range(len(w))] for k in range(len(v))]
    Backtrack = [[[0 for i in range(len(u))] for j in range(len(w))] for k in range(len(v))]
    ## Fill gap arrows
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            for k in range(1, len(u)):
                s1 = S[i - 1][j][k]
                s2 = S[i][j - 1][k]
                s3 = S[i][j][k - 1]
                s4 = S[i - 1][j - 1][k]
                s5 = S[i - 1][j][k - 1]
                s6 = S[i][j - 1][k - 1]
                s7 = S[i - 1][j - 1][k - 1] + (1 if v[i] == w[j] == u[k] else 0)
                S[i][j][k] = max([s1, s2, s3, s4, s5, s6, s7])
                if S[i][j][k] == s1:
                    Backtrack[i][j][k] = 1
                elif S[i][j][k] == s2:
                    Backtrack[i][j][k] = 2
                elif S[i][j][k] == s3:
                    Backtrack[i][j][k] = 3
                elif S[i][j][k] == s4:
                    Backtrack[i][j][k] = 4
                elif S[i][j][k] == s5:
                    Backtrack[i][j][k] = 5
                elif S[i][j][k] == s6:
                    Backtrack[i][j][k] = 6
                elif S[i][j][k] == s7:
                    Backtrack[i][j][k] = 7
    print(S[i][j][k])
    return Backtrack

def Alignment(Backtrack, v, w, u):
    i = len(Backtrack) - 1
    j = len(Backtrack[0]) - 1
    k = len(Backtrack[0][0]) - 1
    res_v = ''
    res_w = ''
    res_u = ''
    while i > 0 and j > 0 and k > 0:
        if Backtrack[i][j][k] == 7:
            res_v = v[i - 1] + res_v
            res_w = w[j - 1] + res_w
            res_u = u[k - 1] + res_u
            i -= 1
            j -= 1
            k -= 1
        elif Backtrack[i][j][k] == 6:
            res_v = '-' + res_v
            res_w = w[j - 1] + res_w
            res_u = u[k - 1] + res_u
            j -= 1
            k -= 1
        elif Backtrack[i][j][k] == 5:
            res_v = v[i - 1] + res_v
            res_w = w[j - 1] + res_w
            res_u = '-' + res_u
            i -= 1
            j -= 1
        elif Backtrack[i][j][k] == 4:
            res_v = v[i - 1] + res_v
            res_w = '-' + res_w
            res_u = u[k - 1] + res_u
            i -= 1
            k -= 1
        elif Backtrack[i][j][k] == 3:
            res_v = '-' + res_v
            res_w = '-' + res_w
            res_u = u[k - 1] + res_u
            k -= 1
        elif Backtrack[i][j][k] == 2:
            res_v = '-' + res_v
            res_w = w[j - 1] + res_w
            res_u = '-' + res_u
            j -= 1
        else:
            res_v = v[i - 1] + res_v

            res_w = '-' + res_w
            res_u = '-' + res_u
            i -= 1
    print(res_v)
    print(res_w)
    print(res_u)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    v = lines[0].rstrip()
    w = lines[1].rstrip()
    u = lines[2].rstrip()
    Backtrack = TripleAlignment(v, w, u)
    Alignment(Backtrack, v, w, u)