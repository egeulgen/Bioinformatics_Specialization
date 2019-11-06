import sys

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

if __name__ == "__main__":
    BWT = sys.stdin.read().rstrip()
    print(InverseBurrowsWheelerTransform(BWT))