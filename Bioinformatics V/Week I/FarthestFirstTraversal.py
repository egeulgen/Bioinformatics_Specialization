import sys

def Euclidean_distance(PointA, PointB):
    ''' Calculate Euclidean Distance
    Input: Two lists with the same lengths,
    PointA and PointB (with dimension m)

    Output: The Euclidean distance between
    the two points
    '''
    if len(PointA) != len(PointB):
        raise ValueError('The dimensions are not the same!')

    dist = 0
    for i in range(len(PointA)):
        dist += ((PointA[i] - PointB[i]) ** 2)
    dist **= 1/2

    return dist

def dist_from_centers(DataPoint, Centers):
    ''' Calculate Distance from Centers
    Input: DataPoint, a single point with m dimensions
    Centers, a list of center points, each with dimension m

    Output: The minimum Euclidean distance between DataPoint
    and all of the Centers.
    '''
    min_d = float("inf")
    for C in Centers:
        distance = Euclidean_distance(DataPoint, C)
        if distance < min_d:
            min_d = distance
    return min_d

def FarthestFirstTraversal(Data, k):
    ''' Farthest First Traversal
    '''
    Centers = [Data[0]]
    while len(Centers) < k:
        max_d = 0
        for DataPoint in Data:
            if DataPoint not in Centers:
                current = dist_from_centers(DataPoint, Centers)
                if current > max_d:
                    max_d = current
                    nextCenter = DataPoint
        Centers.append(nextCenter)
    return Centers


if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    k, m = [int(x) for x in tmp[0].split(' ')] ## numbers of partitions, dimensions\

    Data = []
    for i in range(1, len(tmp)):
        Data.append([float(d) for d in tmp[i].split(' ')])

    Centers = FarthestFirstTraversal(Data, k)
    
    for C in Centers:
        print(' '.join([str(x) for x in C]))