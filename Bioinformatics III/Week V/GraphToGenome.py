def CycleToChromosome(Nodes):
    Chromosome = []
    for i in range(0, len(Nodes), 2):
        if Nodes[i] < Nodes[i + 1]:
            Chromosome.append(Nodes[i + 1] // 2)
        else:
            Chromosome.append(-Nodes[i] // 2)
    return Chromosome

def GraphToGenome(GenomeGraph):
    P = []
    Cycles = []
    temp = []
    for i in range(len(GenomeGraph)):
        if i == len(GenomeGraph) - 1:
            temp += GenomeGraph[i]
            Cycles.append(temp)
        elif GenomeGraph[i][1] == GenomeGraph[i + 1][0] + 1 or GenomeGraph[i][1] == GenomeGraph[i + 1][0] -1:
            temp += GenomeGraph[i]
        else:
            temp += GenomeGraph[i]
            Cycles.append(temp)
            temp = []
    for Cycle in Cycles:
        Chromosome = CycleToChromosome([Cycle[-1]] + Cycle[:-1])
        P.append(Chromosome)
    return P

if __name__ == "__main__":
    GenomeGraph = input().rstrip()
    GenomeGraph = GenomeGraph[1:-1]
    GenomeGraph = GenomeGraph.split('), (')
    for i in range(len(GenomeGraph)):
        GenomeGraph[i] = GenomeGraph[i].split(', ')
        for j in range(len(GenomeGraph[i])):
            GenomeGraph[i][j] = int(GenomeGraph[i][j])
    result = GraphToGenome(GenomeGraph)
    for j in range(len(result)):
        result[j] = '(' + ' '.join(('+' if i > 0 else '') + str(i) for i in result[j]) + ')'
    print(''.join(result))
