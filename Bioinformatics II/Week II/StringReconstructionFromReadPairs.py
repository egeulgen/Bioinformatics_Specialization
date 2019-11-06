def DeBruijnGraphFromKmers(PairedReads):
    adj_list = []
    for paired_read in PairedReads:
        node_from = (paired_read[0][:-1], paired_read[1][:-1])
        node_to = (paired_read[0][1:], paired_read[1][1:])
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
    path = cycle[idx + 1:] + cycle[1:idx + 1]
    return path

def StringSpelledByGappedPatterns(GappedPatterns, d):
    k = len(GappedPatterns[0][0])
    PrefixString = ''
    SuffixString = ''
    for i, pattern_pair in enumerate(GappedPatterns):
        if i != len(GappedPatterns) - 1:
            PrefixString += pattern_pair[0][0]
            SuffixString += pattern_pair[1][0]
        else:
            PrefixString += pattern_pair[0]
            SuffixString += pattern_pair[1]
    for i in range(k + d + 1, len(PrefixString)):
        if PrefixString[i] != SuffixString[i - k - d - 1]:
            return -1
    return PrefixString + SuffixString[len(SuffixString) - k - d - 1: ]

def StringReconstructionFromReadPairs(k, d, PairedReads):
    adj_list = DeBruijnGraphFromKmers(PairedReads)
    path = EulerianPath(adj_list)
    result = StringSpelledByGappedPatterns(path, d)
    return result

if __name__ == "__main__":
    import sys
    input_list = sys.stdin.read().splitlines()
    PairedReads = []
    for i, line in enumerate(input_list):
        if i == 0:
            k, d = map(int, line.rstrip().split())
        else:
            line = line.rstrip()
            PairedReads.append(line.split('|'))
    print(StringReconstructionFromReadPairs(k, d, PairedReads))






# file = open('example.txt')
# PairedReads = []
# for i, line in enumerate(file):
#     if i == 0:
#         k, d = map(int, line.rstrip().split())
#     else:
#         line = line.rstrip()
#         PairedReads.append(line.split('|'))