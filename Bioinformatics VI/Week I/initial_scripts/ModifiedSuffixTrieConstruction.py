import sys

class Trie:
    ''' Trie Structure
    Each node has target nodes(list), edge_labels (list), positions (list)
    and label (string) attributes.
    Method for adjacency list representation of the tree structure.
    '''
    def __init__(self, idx):
        self.targets = []
        self.edge_labels = []
        self.positions = []
        self.label = str(idx)

    def to_adj_list(self):
        adj_list = []
        for i in range(len(self.targets)):
            target_node = self.targets[i]
            adj_list.append([self.label, target_node.label, self.edge_labels[i], self.positions[i]])
            adj_list += target_node.to_adj_list()
        return adj_list

    def __str__(self):
        res = ''
        for i in range(len(self.targets)):
            target_node = self.targets[i]
            res += self.label + '->' + target_node.label + ':' + self.edge_labels[i] + ':' + str(self.positions[i]) + '\n'
            res += target_node.__str__()
        return res

    def __repr__(self):
        return '<trie adjacency list representation>'

def ModifiedSuffixTrieConstruction(Text):
    ''' Trie Construction
    Function to construct a Trie structure
    for storing Patterns
    ''' 
    root = Trie(0)
    idx = 1
    for i in range(len(Text)):
        currentNode = root
        for j in range(i, len(Text)):
            currentSymbol = Text[j]
            # if there is an outgoing edge from currentNode labeled by currentSymbol
            if currentSymbol in currentNode.edge_labels:
                # currentNode ← ending node of this edge
                for k in range(len(currentNode.edge_labels)):
                    if currentNode.edge_labels[k] == currentSymbol:
                        currentNode = currentNode.targets[k]
                        break
            else:
                # add a new node newNode to Trie
                newNode = Trie(idx)
                idx += 1
                # add a new edge from currentNode to newNode with label currentSymbol
                currentNode.targets.append(newNode)
                # Symbol(newEdge) ← currentSymbol
                currentNode.edge_labels.append(currentSymbol)
                # Position(newEdge) ← j
                currentNode.positions.append(j)
                currentNode = newNode
        # if currentNode is a leaf in Trie, assign label i to this leaf
        if len(currentNode.targets) == 0:
            currentNode.label = 'L' + str(i)

    return root


if __name__ == "__main__":
    Text = sys.stdin.read().rstrip()
    print(ModifiedSuffixTrieConstruction(Text))

