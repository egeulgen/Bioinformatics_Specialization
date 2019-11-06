import sys
import TrieConstruction

def PrefixTrieMatching(Text, root):
    ''' Prefix Trie Matching
    '''
    symbol = Text[0]
    v = root

    idx = 1
    pattern = ''
    while True:
        if len(v.edge_labels) == 0:
            return pattern
        elif symbol in v.edge_labels:
            pattern += symbol
            for i in range(len(v.edge_labels)):
                if v.edge_labels[i] == symbol:
                    v = v.targets[i]
                    break
            if idx != len(Text):
                symbol = Text[idx]
                idx += 1
        else:
            return None

def TrieMatching(Text, root):
    ''' Trie Matching
    '''
    indices = []
    idx = 0
    while len(Text) != 0:
        match = PrefixTrieMatching(Text, root)
        if match != None:
            indices.append(idx)
        Text = Text[1:]
        idx += 1
    return indices

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    Text = tmp[0]
    Patterns = []
    for i in range(1, len(tmp)):
        Patterns.append(tmp[i])

    root = TrieConstruction.TrieConstruction(Patterns)

    result = TrieMatching(Text, root)
    print(' '.join(str(x) for x in result))