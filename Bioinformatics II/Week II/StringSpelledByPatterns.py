def StringSpelledByGappedPatterns(GappedPatterns, d):
    k = len(GappedPatterns[0][0])
    PrefixString = ''
    SuffixString = ''
    for i, pattern_pair in enumerate(GappedPatterns):
        if i != len(GappedPatterns) - 1:
            PrefixString += pattern_pair[0][0]
            SuffixString += pattern_pair[1][0]
        else:
            PrefixString += pattern_pair[0]
            SuffixString += pattern_pair[1]
    for i in range(k + d + 1, len(PrefixString)):
        if PrefixString[i] != SuffixString[i - k - d]:
            return "there is no string spelled by the gapped patterns"
    return PrefixString + SuffixString[len(SuffixString) - k - d: ]

if __name__ == "__main__":
    import sys
    input_list = sys.stdin.read().splitlines()
    GappedPatterns = []
    for i, line in enumerate(input_list):
        if i == 0:
            k, d = map(int, line.rstrip().split())
        else:
            line = line.rstrip()
            GappedPatterns.append(line.split('|'))
    print(StringSpelledByGappedPatterns(GappedPatterns, d))



# file = open('example.txt')
# GappedPatterns = []
# for i, line in enumerate(file):
#     if i == 0:
#         k, d = map(int, line.rstrip().split())
#     else:
#         line = line.rstrip()
#         GappedPatterns.append(line.split('|'))