def DeBruijnGraphFromKmers(kmers):
    adj_list = []
    for kmer in kmers:
        node_from = kmer[:-1]
        node_to = kmer[1:]
        adj_list.append((node_from, node_to))
    return adj_list

def EulerianCycle(adj_list):
    from random import randint
    cycle = []
    for edge in adj_list:
        cycle.append(edge[0])
    cycle = list(set(cycle))
    first_cycle = True
    while len(adj_list) != 0:
        possible_starts = []
        for edge in adj_list:
            if edge[0] in cycle:
                possible_starts.append(edge)
        newStart = possible_starts[randint(0, len(possible_starts) - 1)]
        adj_list.remove(newStart)
        if first_cycle:
            cycle = [newStart[0], newStart[1]]
            first_cycle = False
        else:
            idx = 0
            while cycle[idx] != newStart[0]:
                idx += 1
            cycle = cycle[idx:] + cycle[1:idx + 1]
            cycle.append(newStart[1])
        if len(adj_list) == 0:
            return cycle
        current = [edge for edge in adj_list if edge[0] == newStart[1]]
        current = current[randint(0, len(current) - 1)]
        adj_list.remove(current)
        cycle.append(current[1])
        if len(adj_list) == 0:
            return cycle
        while current[1] != newStart[0]:
            current = [edge for edge in adj_list if edge[0] == current[1]]
            current = current[randint(0, len(current) - 1)]
            adj_list.remove(current)
            cycle.append(current[1])
            if len(adj_list) == 0:
                return cycle
    return cycle

def kUniversalCircularSring(k):
    ## generate kmers
    kmers = []
    for i in range(2 ** k):
        kmer = str(bin(i))[2:]
        if len(kmer) != k:
            kmer = '0' * (k - len(kmer)) + kmer
        kmers.append(kmer)
    ## find the eulerian cycle
    adj_list = DeBruijnGraphFromKmers(kmers)
    res = EulerianCycle(adj_list)
    res = res[:len(res) - k + 1]
    string = res[0][:-1]
    for r in res:
        string += r[-1]
    return string

if __name__ == "__main__":
    import sys
    k = int(sys.stdin.read())
    print(kUniversalCircularSring(k))
