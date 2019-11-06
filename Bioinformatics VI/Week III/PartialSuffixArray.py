import sys

def PartialSuffixArray(Text, K):
    ''' Partial Suffix Array
    Input: A string Text and a positive integer K.
    Output: SuffixArrayK(Text), in the form of a list of ordered pairs (i, SuffixArray(i)) for all nonempty entries in the partial suffix array.
    '''
    suffixes = []
    suffix_array = []
    for i in range(len(Text)):
        suffixes.append(Text[i:])
        suffix_array.append(i)

    suffix_array = [x for _, x in sorted(zip(suffixes, suffix_array), key=lambda pair: pair[0])]

    partial_suffix_array = [(i, x) for i, x in enumerate(suffix_array) if x % K == 0]

    return partial_suffix_array

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    Text = tmp[0]
    K = int(tmp[1])

    partial_suffix_array = PartialSuffixArray(Text, K)
    for elem in partial_suffix_array:
        print(','.join(str(x) for x in elem))