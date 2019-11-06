import networkx as nx
import sys

def DistanceBetweenLeaves(graph, num_leaves, weights):
    dist_mat = [[0 for i in range(num_leaves)] for j in range(num_leaves)]
    for i in range(num_leaves - 1):
        for j in range(i + 1, num_leaves):
            spath = nx.shortest_path(graph, source = str(i), target = str(j))
            dist = 0
            for k in range(len(spath) - 1):
                key = '->'.join(spath[k:k + 2])
                dist += weights[key]
            dist_mat[i][j] = dist
            dist_mat[j][i] = dist
    return dist_mat

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    num_leaves = int(lines[0])
    weights = {}
    graph = nx.Graph()
    for i in range(1, len(lines)):
        line = lines[i]
        nodes, weight = line.split(':')
        node1, node2 = nodes.split('->')
        weights[nodes] = int(weight)
        graph.add_edge(node1, node2)
    result = DistanceBetweenLeaves(graph, num_leaves, weights)
    for row in result:
        print(' '.join(map(str, row)))