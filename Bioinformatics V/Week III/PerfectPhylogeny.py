import sys
import pickle

class Tree:
    ''' Binary Tree Structure
    Each node has left, right, indices and labels attributes.
    + Custom representation method to display the tree
    '''
    def __init__(self):
        self.left = None
        self.right = None
        self.indices = []
        self.labels = []

    def total_depth(self, dep = 0):
        if self.left == None and self.right == None:
            return dep
        dep += max(self.left.total_depth(dep), self.right.total_depth(dep))
        return dep + 1

    def __str__(self, level = 0):
        ret = '|\t' * level + repr(','.join(str(x) for x in self.labels)) + '\n'
        if self.left != None:
            ret += self.left.__str__(level + 1)
        if self.right != None:
            ret += self.right.__str__(level + 1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

def PerfectPhylogeny(SNP_mat, labels):
    ''' Perfect Phylogeny Algorithm
    Create the pyhlohentic tree using the
    Perfect Phylogeny approach.
    '''
    m = len(SNP_mat[0])
    n = len(SNP_mat)

    ## Sort columns into descending lexicographic order
    col_vals = []
    for j in range(m):
        val = ''
        for i in range(n):
            val += str(SNP_mat[i][j])
        col_vals.append(val)

    for i in range(n):
        SNP_mat[i] = [x for _,x in sorted(zip(col_vals, SNP_mat[i]), reverse = True)]

    ## Create phylogenetic tree by splitting into two at each step
    root = Tree()
    root.indices = [i for i in range(n)]
    root.labels = [x for x in labels]
    children = [root]
    for j in range(m):
        # determine Oi and Oi_bar
        O_i = [i for i in range(n) if SNP_mat[i][j] == 1]
        O_i_bar = [i for i in range(n) if SNP_mat[i][j] == 0]
        # choose a child v if Oi is a subset of the individuals contained in Tv
        for v in children:
            if set(O_i).issubset(v.indices):
                break
        # if Oi is equal to the individuals assigned to v, then we stop
        if O_i == v.indices:
            break
        else:
            v.left = Tree()
            v.left.indices = [i for i in O_i if i in v.indices]
            v.left.labels = [labels[i] for i in O_i if i in v.indices]
            v.right = Tree()
            v.right.indices = [i for i in O_i_bar if i in v.indices]
            v.right.labels = [labels[i] for i in O_i_bar if i in v.indices]
            children = [v.left, v.right]

    return root


if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()

    SNP_mat = []
    individuals = []
    for i in range(len(tmp)):
        SNP_mat.append([int(s) for s in tmp[i].rstrip().split(' ')[1:]])
        individuals.append(tmp[i].rstrip().split(' ')[0])

    result = PerfectPhylogeny(SNP_mat, individuals)
    print(result)

    pickle.dump( result, open( "phylo_tree.pickle", "wb" ) )
