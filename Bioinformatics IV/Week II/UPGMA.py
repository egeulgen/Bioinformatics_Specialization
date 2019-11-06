import sys

def UPGMA(dist_mat, num_leaves):
    dist_dict = {}
    for i in range(len(dist_mat)):
        dist_dict[i] = {}
        for j in range(len(dist_mat[i])):
            dist_dict[i][j] = dist_mat[i][j]

    Clusters = {}
    for i in range(len(dist_mat)):
        Clusters[i] = [i]

    ages = {}
    for i in range(len(dist_mat)):
        ages[i] = 0.0

    new_node = num_leaves - 1

    T = []
    while len(dist_dict) > 1:
        min_d = 1e6
        nodes = list(dist_dict.keys())
        for i in range(len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                if dist_dict[nodes[i]][nodes[j]] < min_d:
                    min_d = dist_dict[nodes[i]][nodes[j]]
                    node_i = nodes[i]
                    node_j = nodes[j]

        new_clu = Clusters[node_i] + Clusters[node_j]
        new_node += 1
        T.append([new_node, node_i])
        T.append([new_node, node_j])

        ages[new_node] = dist_dict[node_i][node_j] / 2

        dist_dict[new_node] = {}
        dist_dict[new_node][new_node] = 0
        for old_node in nodes:
            total = 0
            count = 0
            for init_node in Clusters[old_node]:
                for node in new_clu:
                    total += dist_mat[init_node][node]
                    count += 1
            dist_dict[old_node][new_node] = total / count
            dist_dict[new_node][old_node] = total / count
        
        Clusters[new_node] = new_clu

        del dist_dict[node_i]
        del dist_dict[node_j]
        for key in dist_dict.keys():
            del dist_dict[key][node_i]

        for key in dist_dict.keys():
            del dist_dict[key][node_j]

    final_tree = []
    for edge in T:
        length = ages[edge[0]] - ages[edge[1]]
        final_tree.append(edge + [length])
        final_tree.append(edge[::-1] + [length])
    final_tree.sort(key = lambda x: x[1])
    final_tree.sort(key = lambda x: x[0])
    return final_tree



if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    num_leaves = int(lines[0])
    dist_mat = []
    for row in lines[1:]:
        temp = row.rstrip().split(' ')
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        dist_mat.append(temp)
    result = UPGMA(dist_mat, num_leaves)
    for edge in result:
        print(str(edge[0]) + '->' + str(edge[1]) + ':' + '%.3f' % edge[2])