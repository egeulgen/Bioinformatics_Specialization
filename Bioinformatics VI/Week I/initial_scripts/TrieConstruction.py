import sys

class Trie:
    ''' Trie Structure
    Each node has target nodes(list) and edge_labels (list)
    attributes.
    Method for adjacency list representation of the trie structure.
    '''
    def __init__(self, idx):
        self.targets = []
        self.edge_labels = []
        self.label = str(idx)

    def __str__(self):
        res = ''
        for i in range(len(self.targets)):
            target_node = self.targets[i]
            res += self.label + '->' + target_node.label + ':' + self.edge_labels[i] + '\n'
            res += target_node.__str__()
        return res

    def __repr__(self):
        return '<trie adjacency list representation>'

def TrieConstruction(Patterns):
    ''' Trie Construction
    Function to construct a Trie structure
    for storing Patterns
    ''' 
    root = Trie(0)
    idx = 1
    for Pattern in Patterns:
        currentNode = root
        for i in range(len(Pattern)):
            currentSymbol = Pattern[i]
            # if there is an outgoing edge from currentNode with label currentSymbol
            if currentSymbol in currentNode.edge_labels:
                for i in range(len(currentNode.edge_labels)):
                    if currentNode.edge_labels[i] == currentSymbol:
                        currentNode = currentNode.targets[i]
                        break
            else:
                # add a new node newNode to Trie
                newNode = Trie(idx)
                idx += 1
                # add a new edge from currentNode to newNode with label currentSymbol
                currentNode.edge_labels.append(currentSymbol)
                currentNode.targets.append(newNode)
                currentNode = newNode
    return root


if __name__ == "__main__":
    Patterns = sys.stdin.read().splitlines()
    print(TrieConstruction(Patterns))