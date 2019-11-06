import sys

ordinal_keys = {'W': 0, 'X': 1, 'Y': 2, 'Z': 3}

def print_dist_dict(dist_dict):
    all_keys = list(dist_dict.keys())
    for i in range(len(all_keys)):
        all_keys[i] = str(all_keys[i])
    all_keys.sort()

    for i in range(len(all_keys)):
        if all_keys[i] == '4':
            all_keys[i] = 4
        elif all_keys[i] == '5':
            all_keys[i] = 5   

    print('  '.join([' '] + [str(n) for n in all_keys]))
    for node in all_keys:
        row = []
        for node2 in all_keys:
            row.append(dist_dict[node][node2])
        print('  '.join([str(node)] + [str(val) + ' '*(len(str(abs(val))) - 3) for val in row]))
    print('')
    return None

def TotalDistance(dist_dict, i):
    return sum(dist_dict[i].values())

def ConstructNJMatrix(dist_dict):
    D_NJ = {}
    for key1, val1 in dist_dict.items():
        for key2, val in dist_dict[key1].items():
            if not key1 in D_NJ:
                D_NJ[key1] = {}
            if key1 == key2:
                D_NJ[key1][key2] = 0
            else:
                D_NJ[key1][key2] = (len(dist_dict) - 2) * val - TotalDistance(dist_dict, key1) - TotalDistance(dist_dict, key2)
    return D_NJ

def NeighborJoining(dist_dict, num_leaves):
    if num_leaves == 2:
        idx1 = list(dist_dict.keys())[0]
        idx2 = list(dist_dict.keys())[1]
        T = [[idx1, idx2, dist_dict[idx1][idx2]], [idx2, idx1, dist_dict[idx1][idx2]]]
        return T

    D_NJ = ConstructNJMatrix(dist_dict)
    print_dist_dict(D_NJ)

    min_dist = 1e6
    for key1, val1 in D_NJ.items():
        for key2, val in D_NJ[key1].items():
            if key1 != key2 and val < min_dist:
                idx1 = key1
                idx2 = key2
                min_dist = val

    delta = (TotalDistance(dist_dict, idx1) - TotalDistance(dist_dict, idx2)) / (num_leaves - 2)
    LimbLength1 = (dist_dict[idx1][idx2] + delta) / 2
    LimbLength2 = (dist_dict[idx1][idx2] - delta) / 2

    m = max([ordinal_keys[key] if key in ordinal_keys else key for key in list(dist_dict.keys())]) + 1

    for k in dist_dict.keys():
        dist_dict[k][m] = (dist_dict[idx1][k] + dist_dict[k][idx2] - dist_dict[idx1][idx2]) / 2

    dist_dict[m] = {}
    for k in dist_dict.keys():
        dist_dict[m][k] = (dist_dict[idx1][k] + dist_dict[k][idx2] - dist_dict[idx1][idx2]) / 2

    dist_dict[m][m] = 0.0

    del dist_dict[idx1]
    del dist_dict[idx2]

    for k in dist_dict.keys():
        del dist_dict[k][idx1]
        del dist_dict[k][idx2]

    print_dist_dict(dist_dict)
    print('')

    T = NeighborJoining(dist_dict, num_leaves - 1)

    T.append([idx1, m, LimbLength1])
    T.append([m, idx1, LimbLength1])
    T.append([idx2, m, LimbLength2])
    T.append([m, idx2, LimbLength2])

    return T

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    num_leaves = int(lines[0])

    labels = lines[1].split('\t')[1:]

    dist_dict = {}
    for i, row in enumerate(lines[2:]):
        lab = labels[i]
        dist_dict[lab] = {}
        temp = row.rstrip().split('\t')[1:]
        for j in range(len(temp)):
            lab2 = labels[j]
            dist_dict[lab][lab2] = int(temp[j])

    result = NeighborJoining(dist_dict, num_leaves)

    for edge in result:
        print(str(edge[0]) + '->' + str(edge[1]) + ':' + '%.3f' % edge[2])