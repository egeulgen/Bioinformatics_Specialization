import sys

def BWMatching_wrapper(BWT, pattern_list):

    counts = {}
    BWT_list = []
    for char in BWT:
        if char not in counts.keys():
            counts[char] = 1
        else:
            counts[char] += 1
        tmp = char + str(counts[char])
        BWT_list.append(tmp)

    first_col = sorted(BWT_list, key=lambda x: x[0])

    last_to_first = []
    for sym_last in BWT_list:
        for idx, sym_first in enumerate(first_col):
            if sym_first == sym_last:
                last_to_first.append(idx)

    result = []
    for pattern in pattern_list:
        result.append(BWMatching(BWT, pattern, last_to_first))

    return result

def BWMatching(last_column, pattern, last_to_first):
    ''' Burrows Wheeler Matching
    BWMatching(LastColumn, Pattern, LastToFirst)
        top ← 0
        bottom ← |LastColumn| − 1
        while top ≤ bottom
            if Pattern is nonempty
                symbol ← last letter in Pattern
                remove last letter from Pattern
                if positions from top to bottom in LastColumn contain an occurrence of symbol
                    topIndex ← first position of symbol among positions from top to bottom in LastColumn
                    bottomIndex ← last position of symbol among positions from top to bottom in LastColumn
                    top ← LastToFirst(topIndex)
                    bottom ← LastToFirst(bottomIndex)
                else
                    return 0
            else
                return bottom − top + 1
    '''
    top = 0
    bottom = len(last_column) - 1

    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            # if positions from top to bottom in LastColumn 
            # contain any occurrence of symbol

            match_positions = []
            for idx in range(top, bottom + 1):
                if last_column[idx] == symbol:
                    match_positions.append(idx)

            if len(match_positions) != 0:
                top = last_to_first[min(match_positions)]
                bottom = last_to_first[max(match_positions)]
            else:
                return 0
        else:
            return bottom - top + 1

if __name__ == "__main__":
    ''' BW Matching Implementation
    Input: A string BWT(Text), followed by a collection of Patterns.
    Output: A list of integers, where the i-th integer corresponds to the number of 
    substring matches of the i-th member of Patterns in Text.
    '''
    tmp = sys.stdin.read().splitlines()
    BWT = tmp[0]
    pattern_list = tmp[1].split(' ')

    match_nums = BWMatching_wrapper(BWT, pattern_list)
    print(' '.join(str(num) for num in match_nums))
    