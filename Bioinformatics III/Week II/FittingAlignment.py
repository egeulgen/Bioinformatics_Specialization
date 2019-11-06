def FittingAlignment(v, w):
    v = '-' + v
    w = '-' + w
    S = [[0 for i in range(len(w))] for j in range(len(v))]
    Backtrack = [[0 for i in range(len(w))] for j in range(len(v))]
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            diag = S[i - 1][j - 1] + (1 if v[i] == w[j] else -1)
            down = S[i - 1][j] - 1
            right = S[i][j - 1] - 1
            S[i][j] = max([down, right, diag])
            if S[i][j] == down:
                Backtrack[i][j] = 1
            elif S[i][j] == right:
                Backtrack[i][j] = 2
            else:
                Backtrack[i][j] = 4
    j = len(w) - 1
    max_score = S[len(v) - 1][j]
    for k in range(len(v)):
        if S[k][j] > max_score:
            max_score = S[k][j]
            i = k
    print(max_score)
    return (Backtrack, i, j)

def PrintAlignment(Backtrack, v, w, i, j):
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
    Backtrack, i, j = FittingAlignment(v, w)
    PrintAlignment(Backtrack, v, w, i, j)
