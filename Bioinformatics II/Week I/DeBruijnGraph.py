def DeBruijnGraphFromGenome(Text, k):
    unique_nodes = set()
    LEN = len(Text) - k + 2
    for i in range(LEN):
        unique_nodes.add(Text[i:(i + k - 1)])
    unique_nodes = list(unique_nodes)
    node_pre = Text[:(k - 1)]
    adj_list = {node_pre: []}
    for i in range(1, LEN):
        node_post = Text[i:(i + k - 1)]
        adj_list[node_pre].append(node_post)
        node_pre = node_post
        if not node_pre in adj_list.keys():
            adj_list[node_pre] = []
    return adj_list

def DeBruijnGraphFromKmers(Patterns):
    adj_list = {}
    for pattern in Patterns:
        node_from = pattern[:-1]
        node_to = pattern[1:]
        if not node_from in adj_list.keys():
            adj_list[node_from] = [node_to]
        else:
            adj_list[node_from].append(node_to)
    return adj_list

if __name__ == "__main__":
    import sys
    Patterns = sys.stdin.read().splitlines()
    res = DeBruijnGraphFromKmers(Patterns)
    for key, val in res.iteritems():
        if len(val) != 0:
            temp = ', '.join(val)
            print(key + ' -> ' + temp)