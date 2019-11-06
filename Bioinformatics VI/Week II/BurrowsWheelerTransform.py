import sys

def BurrowsWheelerTransform(Text):
    ''' Burrows Wheeler Transform Construction
    Input: A string Text.
    Output: BWT(Text).
    '''
    n = len(Text)
    rotations = sorted([Text[i:] + Text[:i] for i in range(n)])
    bwt = ''.join([rot[-1] for rot in rotations])
    return bwt

if __name__ == "__main__":
    Text = sys.stdin.read().rstrip()
    BWT = BurrowsWheelerTransform(Text)
    print(BWT)