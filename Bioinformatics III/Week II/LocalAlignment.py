file = open('PAM250.txt')
file = file.read().split('\n')
keys = file[0].split()
PAM250 = {}
for i in range(1, len(file)):
    temp = file[i].split()
    key2 = temp[0]
    for j, key in enumerate(keys):
        if not key in PAM250:
            PAM250[key] = {key2: int(temp[j + 1])}
        else:
            PAM250[key][key2] = int(temp[j + 1])

def LocalAlignment(v, w):
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
            diag = S[i - 1][j - 1] + PAM250[v[i]][w[j]]
            down = S[i - 1][j] - 5
            right = S[i][j - 1] - 5
            S[i][j] = max([0, down, right, diag])
            if S[i][j] == 0:
                Backtrack[i][j] = 0
            elif S[i][j] == down:
                Backtrack[i][j] = 1
            elif S[i][j] == right:
                Backtrack[i][j] = 2
            else:
                Backtrack[i][j] = 4
    # for row in S:
    #     print(' '.join(map(str, row)))
    max_score = -1
    for row in S:
        tmp = max(row)
        if tmp > max_score:
            max_score = tmp
    print(max_score)
    return (Backtrack, S)

def Alignment(Backtrack, S, v, w):
    max_val = -1000
    for r, row in enumerate(S):
        for c, val in enumerate(row):
            if S[r][c] > max_val:
                max_val = S[r][c]
                i = r
                j = c  
    res_v = ''
    res_w = ''
    while Backtrack[i][j] != 0:
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
    v = input().rstrip()
    w = input().rstrip()
    Backtrack, S = LocalAlignment(v, w)
    Alignment(Backtrack, S, v, w)