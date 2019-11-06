import networkx as nx
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

def AdditivePhylogeny(dist_mat, num_leaves, graph, int_node):

    if num_leaves == 2:
        graph.add_edge(0, 1, weight = dist_mat[0][1])
        return graph

    n = num_leaves - 1
    len_limb = LimbLength(dist_mat, num_leaves, n)

    for j in range(n):
        dist_mat[j][n] -= len_limb
        dist_mat[n][j] = dist_mat[j][n]

    other_leaves = [i for i in range(num_leaves) if i != n]
    for idx1 in range(len(other_leaves) - 1):
        i = other_leaves[idx1]
        for idx2 in range(idx1 + 1, len(other_leaves)):
            k = other_leaves[idx2]
            if dist_mat[i][n] + dist_mat[n][k] == dist_mat[i][k]:
                selected_i = i
                selected_k = k
    x = dist_mat[selected_i][n]

    del dist_mat[-1]
    for i in range(len(dist_mat)):
        del dist_mat[i][-1]

    while int_node in list(graph.nodes):
        int_node += 1
    T = AdditivePhylogeny(dist_mat, num_leaves - 1, graph, int_node)

    V = -1
    spath = nx.shortest_path(T, source = selected_i, target = selected_k)
    dist = 0
    for j in range(1, len(spath) - 1):
        dist += T[spath[j - 1]][spath[j]]['weight']
        if dist == x:
            V = spath[j]

    if V == -1:
        V = int_node
        while V in list(T.nodes):
            V += 1
        dist = 0
        j = 0
        while dist < x:
            j += 1
            pdist = dist
            dist += T[spath[j - 1]][spath[j]]['weight']
        T.remove_edge(spath[j - 1], spath[j])
        T.add_edge(V, spath[j], weight = dist - x)
        T.add_edge(V, spath[j - 1], weight = x - pdist)

    T.add_edge(V, n, weight = len_limb)

    return T
        

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    num_leaves = int(lines[0])
    dist_mat = []
    for row in lines[1:]:
        temp = row.split(' ')
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        dist_mat.append(temp)
    graph = nx.Graph()
    result = AdditivePhylogeny(dist_mat, num_leaves, graph, num_leaves)
    adj_dict = nx.to_dict_of_lists(result)
    answer = []
    for key, value in adj_dict.items():
        for val in value:
            temp = str(key) + '->' + str(val) + ':' + str(int(result[key][val]['weight']))
            answer.append(temp)
    answer.sort()
    for l in answer:
        print(l)
