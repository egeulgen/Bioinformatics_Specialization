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

def ModifiedAlignment(v, w):
    v = '-' + v
    w = '-' + w
    S_previous = [0] * len(v)
    for i in range(1, len(v)):
        S_previous[i] = S_previous[i - 1] - 5
    j = 1
    while j < len(w):
        S_current = [-5 * j] * len(v)
        for i in range(1, len(v)):
            diag = S_previous[i - 1] + BLOSUM62[v[i]][w[j]]
            vert = S_current[i - 1] - 5
            horiz = S_previous[i] - 5
            S_current[i] = max([diag, vert, horiz])
        S_previous = S_current
        j += 1
    return S_previous

def MiddleEdge(v, w, top = 0, bottom = None, left = 0, right = None):
    if bottom == None:
        bottom = len(v)
    if right == None:
        right = len(w)
    mid_col = (right + left) // 2
    FromSource = ModifiedAlignment(v[top:bottom], w[left:mid_col])
    ToSink = ModifiedAlignment(v[top:bottom][::-1], w[mid_col:right][::-1])[::-1]
    max_len = -1e6
    for i in range(len(FromSource)):
        current = FromSource[i] + ToSink[i]
        if current > max_len:
            max_len = current
            idx = i
    FromSource2 = ModifiedAlignment(v[top:bottom], w[left:mid_col + 1])
    ToSink2 = ModifiedAlignment(v[top:bottom][::-1], w[mid_col + 1:right][::-1])[::-1]
    max_len = -1e6
    for i in range(len(FromSource2)):
        current = FromSource2[i] + ToSink2[i]
        if current > max_len:
            max_len = current
            idx2 = i
    if idx2 == idx + 1:
        return ('D', [idx + top, mid_col], [idx + top + 1, mid_col + 1])
    elif idx2 == idx:
        return ('H', [idx + top, mid_col], [idx + top, mid_col + 1])
    else:
        return ('V', [idx + top, mid_col], [idx + top + 1, mid_col])


if __name__ == "__main__":
    v = input().rstrip()
    w = input().rstrip()
    mid_edge, mid_from, mid_to = MiddleEdge(v, w)
    res = (mid_from, mid_to)
    result = ''
    for r in res:
        result += '(' + str(r[0]) + ', ' + str(r[1]) + ') '
    print(result)