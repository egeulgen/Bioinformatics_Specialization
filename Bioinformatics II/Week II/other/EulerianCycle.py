def ParseAdjacencyList(Adj_list):
    from re import split
    adj_dict = {}
    for elem in Adj_list:
        temp = split(' -> ', elem)
        adj_dict[int(temp[0])] = []
        temp[1] = temp[1].split(',')
        for t in temp[1]:
            adj_dict[int(temp[0])].append(int(t))
    return adj_dict

def EulerianCycle(Adj_list):
    from random import randint
    from copy import deepcopy
    adj_dict = ParseAdjacencyList(Adj_list)
    ## Count total number of edges
    tot_edges = 0
    for sl in adj_dict.values():
        tot_edges += len(sl)
    ## Track number of edges visited
    available_nodes = list(adj_dict.keys())
    while len(available_nodes) != 0:
        idx = randint(0, len(available_nodes) - 1)
        available_edges = deepcopy(adj_dict)
        chosen_node = available_nodes[idx]
        idx = randint(0, len(adj_dict[chosen_node]) - 1)
        current_node = adj_dict[chosen_node][idx]
        available_edges[chosen_node].remove(current_node)
        cycle = [chosen_node, current_node]
        while current_node != chosen_node:
            idx = randint(0, len(available_edges[current_node]) - 1)
            next_node = available_edges[current_node][idx]
            available_edges[current_node].remove(next_node)
            current_node = next_node
            cycle.append(current_node)
        for key, item in available_edges.items():
            available_nodes = []
            if len(item) != 0:
                available_nodes.append(key)

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