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

if __name__ == "__main__":
    Chromosome = input().rstrip()
    Chromosome = Chromosome[1:-1].split(' ')
    for i in range(len(Chromosome)):
        Chromosome[i] = int(Chromosome[i])
    result = ChromosomeToCycle(Chromosome)
    print('(' + ' '.join(map(str, result)) + ')')
