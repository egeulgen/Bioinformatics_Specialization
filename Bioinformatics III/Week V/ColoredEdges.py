def ChromosomeToCycle(Chromosome):
    Nodes = []
    for block in Chromosome:
        if block > 0:
            Nodes.append(2 * block - 1)
            Nodes.append(2 * block)
        else:
            Nodes.append(-2 * block)
            Nodes.append(-2 * block - 1)
    return Nodes

def ColoredEdges(P):
    Edges = []
    for Chromosome in P:
        Nodes = ChromosomeToCycle(Chromosome)
        for j in range(1, len(Nodes), 2):
            if j != len(Nodes) - 1:
                Edges.append([Nodes[j], Nodes[j + 1]])
            else:
                Edges.append([Nodes[j], Nodes[0]])
    return Edges

if __name__ == "__main__":
    P = input().rstrip()
    P = P[1:-1]
    P = P.split(')(')
    for i in range(len(P)):
        P[i] = P[i].split(' ')
        for j in range(len(P[i])):
            P[i][j] = int(P[i][j])
    result = ColoredEdges(P)
    for j in range(len(result)):
        result[j] = '(' + ', '.join(str(i) for i in result[j]) + ')'
    print(', '.join(result))