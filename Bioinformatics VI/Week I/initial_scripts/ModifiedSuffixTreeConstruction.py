import sys
import ModifiedSuffixTrieConstruction

class Tree:
    ''' Tree Structure
    Each node has targets(list), positions (list), lengths (list), 
    and label (string) attributes. 
    Also, method for printing the tree as an adjacency list.
    '''
    def __init__(self, idx):
        self.targets = []
        self.positions = []
        self.lengths = []
        self.label = str(idx)

    def __str__(self):
        res = ''
        for i in range(len(self.targets)):
            target_node = self.targets[i]
            res += self.label + '->' + target_node.label + ':' + str(self.positions[i]) + ':' + str(self.lengths[i]) + '\n'
            res += target_node.__str__()
        return res

    def __repr__(self):
        return '<tree adjacency list representation>'

def ModifiedSuffixTreeConstruction(Text):
    ''' Suffix Tree Construction
    Function to construct a suffix tree structure
    ModifiedSuffixTreeConstruction(Text)
         Trie ← ModifiedSuffixTrieConstruction
         for each non-branching path Path in Trie
             substitute Path by a single edge e connecting the first and last nodes of Path
             Position(e) ← Position(first edge of Path)
             Length(e) ← number of edges of Path
         return Trie
    '''

    trie_root = ModifiedSuffixTrieConstruction.ModifiedSuffixTrieConstruction(Text)
    currentNode = trie_root
    tree_root = Tree(currentNode.label)
    current_tree_node = tree_root
    first_node_pos = currentNode.positions[0] # initializing Position(first edge of Path)
    currentNode.positions.remove(first_node_pos)
    current_length = 0 # initializing number of edges in Path to be added to the tree

    branching_flag = False # to indicate if the node is branching

    tmp_trie_nodes = [] # list to store trie source nodes to return to
    tmp_tree_nodes = [] # list to store tree nodes to return to

    while True:
        next_nodes = currentNode.targets

        # if out degree is > 1
        if len(next_nodes) > 1:
            tmp_trie_nodes.append(currentNode)
            tmp_tree_nodes.append(current_tree_node)

            branching_flag = True

        # select next node (first target node), remove next node from current node
        nxt_node = next_nodes[0]
        currentNode.targets.remove(nxt_node)
        current_length += 1

        # if next node is leaf
        if len(nxt_node.targets) == 0:

            # create end node
            end_node = Tree(nxt_node.label)

            # add end node, position and 
            # length of path from current_tree_node to end_node
            current_tree_node.targets.append(end_node)
            current_tree_node.positions.append(first_node_pos)
            current_tree_node.lengths.append(current_length)

            # reset current length to 0
            current_length = 0

            if len(tmp_trie_nodes) == 0:
                return tree_root
            # reset current tree and trie nodes
            currentNode = tmp_trie_nodes.pop()
            current_tree_node = tmp_tree_nodes.pop()
        
            # reset first node position
            first_node_pos = currentNode.positions[0]
            currentNode.positions.remove(first_node_pos)

        # if next node is non-branching
        elif len(nxt_node.targets) == 1:
            currentNode = nxt_node

        # if next node is branching
        else:
            # create inter. node
            int_node = Tree(nxt_node.label)

            # add inter. node, position and 
            # length of path from current_tree_node to int_node
            current_tree_node.targets.append(int_node)
            current_tree_node.positions.append(first_node_pos)
            current_tree_node.lengths.append(current_length)

            # set current node to next node
            currentNode = nxt_node
            current_tree_node = int_node
            first_node_pos = currentNode.positions[0]
            currentNode.positions.remove(first_node_pos)

            current_length = 0

    return tree_root


if __name__ == "__main__":
    Text = sys.stdin.read().rstrip()
    print(ModifiedSuffixTreeConstruction(Text))
