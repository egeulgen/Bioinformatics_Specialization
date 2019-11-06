import sys
from random import randint

def Diff(S_collection, T_collection):
    ''' Calculate Diff
    Input: SNP sets S’ and T

    Output: Diff(S’, T), quantification of the 
    informativeness of the subset S’ with respect 
    to T, simply sum of Diff(S’, t) over all SNPs 
    t in T.
    '''

    ## number of individuals
    n = len(T_collection[0]) 

    difference = 0

    ## Iterate over all SNPs t in T
    for t in T_collection:
        diff_S_t = 0
        diff_t = 0

        ## For individuals (i,j) if t[i] != t[j]
        # and if s[i] != s[j] for any s in S’,
        # increase the total by 1
        for i in range(n):
            for j in [x for x in range(n) if x != i]:
                if t[i] != t[j]:
                    diff_t += 1
                    for s in S_collection:
                        if s[i] != s[j]:
                            diff_S_t += 1
                            break
        difference += diff_S_t / diff_t

    return difference

def RandomizedHaplotypeSearch(S, T, k):
    ''' Randomized Haplotype Search
    k-Most Informative SNP Problem: 
    Identify a subset of most informative SNPs with respect 
    to another collection of other SNPs.

    Input: SNP matrices corresponding to two 
    collections of SNPs S and T, along with an integer k.

    Output: A subset S’ of S containing k SNPs maximizing 
    Diff(S, T) over all possible choices of S with k SNPs.

    Start with a random collection of k SNPs in S. At each 
    step, try every possible replacement of one SNP in the 
    current collection with some SNP not in the collection 
    and update S’ to be the set that maximizes Diff(S’, T).
    Continue iterating until obtaining a set such that no 
    SNP replacement can increase Diff(S’, T).
    '''

    ## Start with a random collection of k SNPs from S
    bestSNPs = []
    available = [s for s in S]
    while len(bestSNPs) != k:
        chosen = available[randint(0, len(available) - 1)]
        available = [s for s in available if s != chosen] ## assuming non-duplicate snps in S
        bestSNPs.append(chosen)

    ## Iterate until Diff(S’, T) cannot be increased
    while True:
        currentSNPs = [x for x in bestSNPs]

        ## Replace each SNP vector in currentSNPs with another from S
        for s in currentSNPs:
            for s_prime in [x for x in S if x not in currentSNPs]:
                ## S’ := currentSNPs with s replaced by s’
                S_pr = [s_prime if x == s else x for x in currentSNPs]
                ## Keep S_pr with maximum Diff(S’, T)
                if Diff(S_pr, T) > Diff(bestSNPs, T):
                    bestSNPs = S_pr

        if bestSNPs == currentSNPs:
            return bestSNPs

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()

    k = int(tmp[0])

    S = []
    T = []
    flag_for_T = False
    for i in range(1, len(tmp)):
        line = tmp[i]
        if line.startswith('-'):
            flag_for_T = True
        elif not flag_for_T:
            s = [int(x) for x in line.split(", ")]
            S.append(s)
        else:
            t = [int(x) for x in line.split(", ")]
            T.append(s)    

    print(RandomizedHaplotypeSearch(S, T, k))