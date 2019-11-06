def ProcessInput(P):
    P = P[1:-1]
    P = P.split(')(')
    for i in range(len(P)):
            P[i] = P[i].split(' ')
            for j in range(len(P[i])):
                P[i][j] = int(P[i][j])
    return P

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

def FindNextEdge(current, edges):
    if len(edges) == 0:
        return -1
    idx = 0
    while not (current[0] in edges[idx] or current[1] in edges[idx]):
        idx += 1
        if idx == len(edges):
            return -1
    return edges[idx]

def TwoBreakDistance(P, Q):
    edgesP = ColoredEdges(P)
    edgesQ = ColoredEdges(Q)
    edges = edgesP + edgesQ
    blocks = set()
    for edge in edges:
        blocks.add(edge[0])
        blocks.add(edge[1])
    Cycles = []
    while len(edges) != 0:
        start = edges[0]
        edges.remove(edges[0])
        Cycle = [start]
        current = FindNextEdge(start, edges)
        while current != -1:
            Cycle.append(current)
            edges.remove(current)
            current = FindNextEdge(current, edges)
        Cycles.append(Cycle)
    return len(blocks) // 2 - len(Cycles)
    
if __name__ == "__main__":
    P = input().rstrip()
    P = ProcessInput(P)
    Q = input().rstrip()
    Q = ProcessInput(Q)
    print(TwoBreakDistance(P, Q))