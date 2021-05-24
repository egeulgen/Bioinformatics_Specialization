def LCSBackTrack(v, w):
    v = '-' + v
    w = '-' + w
    S = [[0 for i in range(len(w))] for j in range(len(v))]
    Backtrack = [[0 for i in range(len(w))] for j in range(len(v))]
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            tmp = S[i - 1][j - 1] + (1 if v[i] == w[j] else 0)
            S[i][j] = max([S[i - 1][j], S[i][j - 1], tmp])
            if S[i][j] == S[i - 1][j]:
                Backtrack[i][j] = 1
            elif S[i][j] == S[i][j - 1]:
                Backtrack[i][j] = 2
            else:
                Backtrack[i][j] = 4

    LCS = []
    while i > 0 and j > 0:
        if Backtrack[i][j] == 4:
            LCS.append(v[i])
            i -= 1
            j -= 1
        elif Backtrack[i][j] == 2:
            j -= 1
        else:
            i -= 1

    return Backtrack

# def OutputLCS(Backtrack, V, i, j):
#     # print(str(i) + '    ' + str(j))
#     if i == 0 or j == 0:
#         return V[i]
#     if Backtrack[i][j] == 1:
#         return OutputLCS(Backtrack, V, i - 1, j)
#     elif Backtrack[i][j] == 2:
#         return OutputLCS(Backtrack, V, i, j - 1)
#     else:
#         return OutputLCS(Backtrack, V, i - 1, j - 1) + V[i]

def OutputLCS(Backtrack, V, i, j):
    LCS = []
    while i > 0 and j > 0:
        if Backtrack[i][j] == 4:
            LCS.append(V[i])
            i -= 1
            j -= 1
        elif Backtrack[i][j] == 2:
            j -= 1
        else:
            i -= 1
    return LCS

if __name__ == "__main__":
    v = input().rstrip()
    w = input().rstrip()
    Backtrack = LCSBackTrack(v, w)
    i = len(Backtrack) - 1
    j = len(Backtrack[0]) - 1
    res = OutputLCS(Backtrack, v, i, j)
    print(''.join(res[::-1]))