def DeBruijnGraphFromKmers(kmers):
    adj_list = []
    for kmer in kmers:
        node_from = kmer[:-1]
        node_to = kmer[1:]
        adj_list.append((node_from, node_to))
    return adj_list

def StringReconstruction(kmers):
    adj_list = DeBruijnGraphFromKmers(kmers)
    result = EulerianPath(adj_list)
    ReconstructedString = result[0][:-1]
    for r in result:
    	ReconstructedString += r[-1]
    return ReconstructedString

def EulerianPath(adj_list):
    differences = {}
    for edge in adj_list:
        node0 = edge[0]
        node1 = edge[1]
        if not node0 in differences.keys():
            differences[node0] = 1
        else:
            differences[node0] += 1
        if not node1 in differences.keys():
            differences[node1] = -1
        else:
            differences[node1] -= 1
    temp = [-1, -1]
    for key, val in differences.items():
        if val < 0:
            temp[0] = key
        elif val > 0:
            temp[1] = key
    temp = tuple(temp)
    adj_list.append(temp)
    cycle = EulerianCycle(adj_list)
    idx = 0
    while (cycle[idx], cycle[idx + 1]) != temp:
        idx += 1
    cycle = cycle[idx + 1:] + cycle[1:idx + 1]
    return cycle

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
        current = [edge for edge in adj_list if edge[0] == newStart[1]]
        current = current[randint(0, len(current) - 1)]
        adj_list.remove(current)
        cycle.append(current[1])
        while current[1] != newStart[0]:
            current = [edge for edge in adj_list if edge[0] == current[1]]
            current = current[randint(0, len(current) - 1)]
            adj_list.remove(current)
            cycle.append(current[1])
    return cycle

if __name__ == "__main__":
    import sys
    kmers = sys.stdin.read().splitlines()
    print(kmers)
    kmers = kmers[1:]
    print(kmers)
    print(StringReconstruction(kmers))



# file = open('example.txt')
# kmers = []
# for i, line in enumerate(file):
#     if i != 0:
#         kmers.append(line.rstrip())