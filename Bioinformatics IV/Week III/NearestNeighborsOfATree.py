import sys
from copy import deepcopy

def NearestNeighbors(adj_list, chosen_edge):

    w, x = [edge for edge in adj_list if edge[0] == chosen_edge[0] and edge != chosen_edge]
    y, z = [edge for edge in adj_list if edge[0] == chosen_edge[1] and edge != chosen_edge[::-1]]

    new_adj1 = deepcopy(adj_list)
    new_adj2 = deepcopy(adj_list)

    ## create nearest neighbour 1
    new_adj1.remove(x)
    new_adj1.remove(x[::-1])
    new_adj1.remove(y)
    new_adj1.remove(y[::-1])

    new_adj1 += [[y[0], x[1]], [x[0], y[1]], [x[1], y[0]], [y[1], x[0]]]

    ## create nearest neighbour 2
    new_adj2.remove(x)
    new_adj2.remove(x[::-1])
    new_adj2.remove(z)
    new_adj2.remove(z[::-1])

    new_adj2 += [[z[0], x[1]], [x[0], z[1]], [x[1], z[0]], [z[1], x[0]]]

    return [new_adj1, new_adj2]

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    chosen_edge = lines[0].rstrip().split(' ')

    adj_list = []
    for row in lines[1:]:
        temp = row.rstrip().split('->')
        adj_list.append(temp)

    res1, res2 = NearestNeighbors(adj_list, chosen_edge)

    for edge in res1:
        print(edge[0] + '->' + edge[1])
        
    print()

    for edge in res2:
        print(edge[0] + '->' + edge[1])