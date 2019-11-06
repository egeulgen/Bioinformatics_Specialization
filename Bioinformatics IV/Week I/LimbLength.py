import sys

def LimbLength(dist_mat, num_leaves, j):
    other_leaves = [i for i in range(num_leaves) if i != j]
    temp = []
    for idx1 in range(len(other_leaves) - 1):
        i = other_leaves[idx1]
        for idx2 in range(idx1 + 1, len(other_leaves)):
            k = other_leaves[idx2]
            temp.append((dist_mat[i][j] + dist_mat[j][k] - dist_mat[i][k]) / 2)
    limb_length = min(temp)
    return int(limb_length)

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    num_leaves = int(lines[0])
    j = int(lines[1])
    dist_mat = []
    for row in lines[2:]:
        temp = row.split(' ')
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        dist_mat.append(temp)
    print(LimbLength(dist_mat, num_leaves, j))