def HammingDistance(p, q):
    mm = [p[i] != q[i] for i in range(len(p))]
    return sum(mm)

# def ImmediateNeighbors(Pattern):
#     Neighborhood = [Pattern]
#     for i in range(len(Pattern)):
#         nuc = Pattern[i]
#         for nuc2 in ['A', 'C', 'G', 'T']:
#             if nuc != nuc2:
#                 pat = list(Pattern)
#                 pat[i] = nuc2
#                 Neighborhood.append(''.join(pat))
#     return Neighborhood

def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return ['A', 'C', 'G', 'T'] 
    Neighborhood = set()
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            for nuc in ['A', 'C', 'G', 'T']:
                Neighborhood.add(nuc + Text)
        else:
            Neighborhood.add(Pattern[0] + Text)
    return Neighborhood

def FrequentWordsWithMismatches(Text, k, d):
    pattern_dict = {}
    max_val = -1
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i+k]
        Neighborhood = Neighbors(Pattern, d)
        for ApproximatePattern in Neighborhood:
            if ApproximatePattern in pattern_dict.keys():
                pattern_dict[ApproximatePattern] += 1
                if pattern_dict[ApproximatePattern] > max_val:
                    max_val = pattern_dict[ApproximatePattern]
            else:
                pattern_dict[ApproximatePattern] = 1
                if pattern_dict[ApproximatePattern] > max_val:
                    max_val = pattern_dict[ApproximatePattern]
    FrequentPatterns = []
    for key, value in pattern_dict.iteritems():
        if value == max_val:
                FrequentPatterns.append(key)
    return FrequentPatterns

FrequentWordsWithMismatches('ATA', 3, 1)

FrequentWordsWithMismatches('GTAAGATGTGCACTGATGTAAGTAAGTAACACTGACGGACGGATGTGGATGTAACACTCACTGTGGACGGATGTGGTAAGACGGTAAGTGCACTGATGACGGTGGTGGATGATGATGTGGATGACGCACTCACTGTAAGTGGATCACTGACGGATGTAAGACGGTGGATGTAAGATGTGGATGATGATGACGCACTGTAAGACGGTAAGTAAGTAAGACGGTGGTGGTGGTAAGACGGTAACACTCACTGTGCACTGACGGATGTAACACTGATCACTCACTGATGTGGTGGTAAGACGGTAAGATGTAAGACGCACTGTGCACTGTAAGATGACGGACGGTGGATCACTGATGACGGTAACACTCACTGACGGTAA', 6, 2)