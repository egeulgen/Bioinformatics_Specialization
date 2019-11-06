def DeBruijnGraphFromKmers(kmers):
    adj_list = []
    for kmer in kmers:
        node_from = kmer[:-1]
        node_to = kmer[1:]
        adj_list.append((node_from, node_to))
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

def ContigGeneration(kmers):
	adj_list = DeBruijnGraphFromKmers(kmers)
	result = MaximalNonBranchingPaths(adj_list)
	contigs = []
	for res in result:
		contig = ''
		for i, edge in enumerate(res):
			if i == 0:
				contig += edge[0]
				contig += edge[1][-1]
			else:
				contig += edge[1][-1]
		contigs.append(contig)
	return contigs

if __name__ == "__main__":
    import sys
    kmers = sys.stdin.read().splitlines()
    adj_list = DeBruijnGraphFromKmers(kmers)
    contigs = ContigGeneration(kmers)
    contigs.sort()
    print(' '.join(contigs))

# kmers = []
# file = open('example.txt')
# for line in file:
#     kmers.append(line.rstrip())