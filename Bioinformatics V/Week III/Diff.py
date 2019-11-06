import sys

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

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()

    S_collection = []
    T_collection = []
    flag_for_T = False
    for i in range(len(tmp)):
        line = tmp[i]
        if line.startswith('-'):
            flag_for_T = True
        elif not flag_for_T:
            s = [int(x) for x in line.split(", ")]
            S_collection.append(s)
        else:
            t = [int(x) for x in line.split(", ")]
            T_collection.append(t)    

    print(S_collection)
    print(T_collection)
    print(Diff(S_collection, T_collection))
    print(round(Diff(S_collection, T_collection), 3))