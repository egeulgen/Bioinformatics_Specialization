def ParseAdjacencyList(Adj_list):
    from re import split
    adj_list = []
    for elem in Adj_list:
        temp = split(' -> ', elem)
        temp[1] = temp[1].split(',')
        for t in temp[1]:
            adj_list.append((int(temp[0]), int(t)))
    return adj_list

def EulerianCycle(Adj_list):
    from random import randint
    adj_list = ParseAdjacencyList(Adj_list)
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
    Adj_list = sys.stdin.read().splitlines()
    res = EulerianCycle(Adj_list)
    print('->'.join(map(str, res)))

# Adj_list = []
# file = open('example.txt')
# for line in file:
#     Adj_list.append(line.rstrip())