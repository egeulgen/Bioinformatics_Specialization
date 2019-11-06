def ParseAdjacencyList(Adj_list):
    from re import split
    adj_list = []
    for elem in Adj_list:
        temp = split(' -> ', elem)
        temp[1] = temp[1].split(',')
        for t in temp[1]:
            adj_list.append((int(temp[0]), int(t)))
    return adj_list

def MaximalNonBranchingPaths(Graph):
    nodes = {}
    for edge in Graph:
        v = edge[0]
        if not v in nodes.keys():
            nodes[v] = [0, 1]
        else:
            nodes[v][1] += 1
        v = edge[1]
        if not v in nodes.keys():
            nodes[v] = [1, 0]
        else:
            nodes[v][0] += 1
    Paths = []
    for v in nodes.keys():
        if nodes[v][0] != 1 or nodes[v][1] != 1:
            if nodes[v][1] > 0:
                outgoing = []
                for edge in Graph:
                    if edge[0] == v:
                        outgoing.append(edge)
                for vw in outgoing:
                    w = vw[1]
                    NonBranchingPath = [vw]
                    Graph.remove((v,w))
                    while nodes[w][0] == nodes[w][1] == 1:
                        for edge in Graph:
                            if edge[0] == w:
                                NonBranchingPath.append(edge)
                                w = edge[1]
                                Graph.remove(edge)
                                break
                    Paths.append(NonBranchingPath)
    while len(Graph) != 0:
        edge = Graph[0]
        current = edge
        previous = edge
        Graph.remove(edge)
        temp = [edge]
        i = 0
        while temp[-1][1] != edge[0]:
            current = Graph[i]
            if current[0] == previous[1]:
                temp.append(current)
                previous = current
                Graph.remove(previous)
                i = 0
            else:
                i += 1
        Paths.append(temp)
    return Paths

if __name__ == "__main__":
    import sys
    Adj_list = sys.stdin.read().splitlines()
    Graph = ParseAdjacencyList(Adj_list)
    res = MaximalNonBranchingPaths(Graph)
    result = []
    for r in res:
        temp = []
        for i,e in enumerate(r):
            if i == 0:
                temp += [e[0], e[1]]
            else:
                temp.append(e[1])
        result.append(temp)
    for r in result:
        print(' -> '.join(map(str, r)))

# Adj_list = []
# file = open('example.txt')
# for line in file:
#     Adj_list.append(line.rstrip())