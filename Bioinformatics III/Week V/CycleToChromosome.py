def CycleToChromosome(Nodes):
    Chromosome = []
    for i in range(0, len(Nodes), 2):
        if Nodes[i] < Nodes[i + 1]:
            Chromosome.append(Nodes[i + 1] // 2)
        else:
            Chromosome.append(-Nodes[i] // 2)
    return Chromosome

if __name__ == "__main__":
    Nodes = input().rstrip()
    Nodes = Nodes[1:-1].split(' ')
    for i in range(len(Nodes)):
        Nodes[i] = int(Nodes[i])
    result = CycleToChromosome(Nodes)
    print('(' + ' '.join(('+' if i > 0 else '') + str(i) for i in result) + ')')
