import sys
from copy import deepcopy

def Euclidean_distance(PointA, PointB):
    if len(PointA) != len(PointB):
        raise ValueError('The dimensions are not the same!')
    dist = 0
    for i in range(len(PointA)):
        dist += ((PointA[i] - PointB[i]) ** 2)
    dist **= 1/2
    return dist

def assign_clusters(Centers, Data):
    clusters = [[] for i in range(len(Centers))]
    for DataPoint in Data:
        min_d = float('inf')
        for i, Center in enumerate(Centers):
            current = Euclidean_distance(DataPoint, Center)
            if current < min_d:
                min_d = current
                idx = i
        clusters[idx].append(DataPoint)
    return clusters

def cluster_mean(cluster):
    m = len(cluster[0])
    clu_mean = [0 for i in range(m)]
    for member in cluster:
        for i in range(m):
            clu_mean[i] += member[i] / len(cluster)
    return clu_mean

def Lloyd_kmeans(Data, k):
    Centers = Data[:k]
    new_centers = [[] for i in range(k)]

    while True:
        clusters = assign_clusters(Centers, Data)
        for i, clu in enumerate(clusters):
            new_centers[i] = cluster_mean(clu)

        if new_centers == Centers:
            break
        Centers = deepcopy(new_centers)

    return Centers

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    k, m = [int(x) for x in tmp[0].split(' ')] ## numbers of partitions, dimensions

    Data = []
    for i in range(1, len(tmp)):
        Data.append([float(d) for d in tmp[i].split(' ')])

    Centers = Lloyd_kmeans(Data, k)
    for C in Centers:
        print(' '.join([str(x) for x in C]))