import sys

def create_check_point_array(BWT, C):
    symbol_list = list(set(BWT))
    check_point_array = {}
    for idx in range(0, len(BWT), C):
        check_point_array[idx] = {}
        for symbol in symbol_list:
            check_point_array[idx][symbol] = BWT[:idx].count(symbol)
    return check_point_array

def Count_symbol(check_point_array, idx, LastColumn, symbol):
    vals = [x for x in check_point_array.keys() if x <= idx]
    nearest_idx = min(vals, key=lambda x: abs(x - idx))

    count = check_point_array[nearest_idx][symbol]
    count += LastColumn[nearest_idx:idx].count(symbol)
    return count

def pattern_to_seeds(pattern, d):

    minsize = len(pattern) // (d + 1)

    cut_points = list(range(0 , len(pattern) - minsize + 1, minsize))
    cut_points.append(len(pattern))

    seeds = []
    offsets = []
    for i in range(1, len(cut_points)):
        seeds.append(pattern[cut_points[i - 1] : cut_points[i]])
        offsets.append(cut_points[i - 1])
    return seeds, offsets

def InverseBurrowsWheelerTransform(BWT):
    ''' Burrows Wheeler Transform Construction
    Input: A string Transform (with a single "$" symbol).
    Output: The string Text such that BWT(Text) = Transform
    '''
    lenText = len(BWT)
    
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

    first_row = ['$1']
    for i in range(1, lenText):
        prev_symbol = first_row[i - 1]
        for BWT_idx, char in enumerate(BWT_list):
            if char == prev_symbol:
                idx = BWT_idx
                break
        first_row.append(first_col[idx])

    Text = ''
    for i in range(1, len(first_row)):
        Text += ''.join(x for x in first_row[i] if not x.isdigit())
    Text += '$'
    return Text

def MultiplePatternMatching(FirstOccurrence, LastColumn, pattern, check_point_array):
    ''' Multiple Pattern Matching with BWT
    '''
    top = 0
    bottom = len(LastColumn) - 1

    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            # if positions from top to bottom in LastColumn 
            # contain any occurrence of symbol
            if symbol in LastColumn[top : bottom + 1]:
                top = FirstOccurrence[symbol] + Count_symbol(check_point_array, top, LastColumn, symbol)
                bottom = FirstOccurrence[symbol] + Count_symbol(check_point_array, bottom + 1, LastColumn, symbol) - 1
            else:
                return False, False
        else:
            return top, bottom

def find_seed_positions(seed, FirstOccurrence, BWT, check_point_array, partial_suffix_array):
    seed_pos_list = []
    top, bottom = MultiplePatternMatching(FirstOccurrence, BWT, seed, check_point_array)
    if top:
        for idx in range(top, bottom + 1):
            to_add = 0
            while idx not in partial_suffix_array.keys():
                idx = FirstOccurrence[BWT[idx]] + Count_symbol(check_point_array, idx, BWT, BWT[idx])
                to_add += 1
            seed_pos_list.append(partial_suffix_array[idx] + to_add)
    return seed_pos_list

def wrapper(d, C):

    with open("myc_bwt.txt") as f:
        for line in f:
            BWT = line.rstrip()

    partial_suffix_array = {}
    with open("myc_psuffarr.txt") as f:
        for line in f:
            tmp = line.rstrip().split(",")
            partial_suffix_array[int(tmp[0])] = int(tmp[1])

    pattern_list = []
    with open("myc_reads.txt") as f:
        for line in f:
            pattern_list.append(line.rstrip())

    FirstOccurrence = {}
    for idx, symbol in enumerate(sorted(BWT)):
        if symbol not in FirstOccurrence.keys():
            FirstOccurrence[symbol] = idx

    check_point_array = create_check_point_array(BWT, C)
    
    Text = InverseBurrowsWheelerTransform(BWT)

    positions_list = []
    for pattern in pattern_list:
        ## break pattern into seeds
        seeds_list, offsets_list = pattern_to_seeds(pattern, d)

        # find exact matches and try to extend each seed
        pattern_pos_list = set()
        for candidate_seed, offset in zip(seeds_list, offsets_list):
            seed_pos_list = find_seed_positions(candidate_seed, FirstOccurrence, BWT, check_point_array, partial_suffix_array)

            for candidate_pos in seed_pos_list:
                pattern_position = candidate_pos - offset

                if pattern_position >= 0 and pattern_position + len(pattern) <= len(Text):
                    approximate_match_flag = True
                    num_mismatch = 0
                    for idx, symbol in enumerate(pattern):
                        if symbol != Text[pattern_position + idx]:
                            num_mismatch += 1
                            if num_mismatch > d:
                                approximate_match_flag = False
                                break
                    if approximate_match_flag:
                        pattern_pos_list.add(pattern_position)

        positions_list += list(pattern_pos_list)
                    
    return sorted(positions_list)

if __name__ == "__main__":

    d = 1
    C = 100

    positions_list = wrapper(d, C)
    print(' '.join(str(pos) for pos in positions_list))
    