import sys

def Euclidean_distance(PointA, PointB):
    if len(PointA) != len(PointB):
        raise ValueError('The dimensions are not the same!')
    dist = 0
    for i in range(len(PointA)):
        dist += ((PointA[i] - PointB[i]) ** 2)
    dist **= 1/2
    return dist

def dist_from_centers(DataPoint, Centers):
    min_d = float("inf")
    for C in Centers:
        distance = Euclidean_distance(DataPoint, C)
        if distance < min_d:
            min_d = distance
    return min_d

def Distortion(Data, Centers):
    distortion = 0
    for DataPoint in Data:
        distortion += (dist_from_centers(DataPoint, Centers) ** 2)
    distortion /= len(Data)
    return distortion

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    k, m = [int(x) for x in tmp[0].split(' ')] ## numbers of partitions, dimensions\

    Centers = []
    for i in range(1, k + 1):
        Centers.append([float(x) for x in tmp[i].split(' ')])

    Data = []
    for i in range(k + 2, len(tmp)):
        Data.append([float(d) for d in tmp[i].split(' ')])

    print(Distortion(Data, Centers))