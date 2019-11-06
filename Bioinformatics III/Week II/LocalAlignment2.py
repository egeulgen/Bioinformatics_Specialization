import sys

def LocalAlignment(v, w):
    v = '-' + v
    w = '-' + w
    S = [[0 for i in range(len(w))] for j in range(len(v))]
    Backtrack = [[0 for i in range(len(w))] for j in range(len(v))]

    for i in range(1, len(v)):
        for j in range(1, len(w)):
            diag = S[i - 1][j - 1] + (6 if v[i] == w[j] else -3)
            down = S[i - 1][j] - 4
            right = S[i][j - 1] - 4
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
    input = sys.stdin.read().splitlines()
    v = input[0]
    w = input[1]
    Backtrack, S = LocalAlignment(v, w)
    Alignment(Backtrack, S, v, w)