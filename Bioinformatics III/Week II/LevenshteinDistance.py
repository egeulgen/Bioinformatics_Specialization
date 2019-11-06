def LevenshteinDistance(v, w):
    v = '-' + v
    w = '-' + w
    S = [[0 for i in range(len(w))] for j in range(len(v))]
    for i in range(1, len(S)):
        S[i][0] = S[i - 1][0] + 1
    for j in range(1, len(S[0])):
        S[0][j] = S[0][j - 1] + 1
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            diag = S[i - 1][j - 1] + (1 if v[i] != w[j] else 0)
            down = S[i - 1][j] + 1
            right = S[i][j - 1] + 1
            S[i][j] = min([down, right, diag])
    return S[len(v) - 1][len(w) - 1]

if __name__ == "__main__":
    v = input().rstrip()
    w = input().rstrip()
    print(LevenshteinDistance(v, w))