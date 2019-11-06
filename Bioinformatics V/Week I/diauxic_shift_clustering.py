import pandas as pd
from copy import deepcopy
import k_means_initializer
import SquaredErrorDistortion

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
    Centers = k_means_initializer.k_means_initializer(Data, k)
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
    # df = pd.read_csv('230genes_log_expression.txt', sep='\t', header=0, na_filter=False)
    df = pd.read_csv('diauxic_raw_ratios_RG.txt', sep='\t', header=0, na_filter=False)
    exp_columns = [x for x in list(df.columns) if x.startswith('R')]

    Data = []
    for index, row in df.iterrows():
        Data.append(list(row[exp_columns]))

    for k in range(6, 7):
        Centers = Lloyd_kmeans(Data, k)
        distortion = SquaredErrorDistortion.Distortion(Data, Centers)
        
        print('For k = %d' % k)
        print('Distortion is %f' % distortion)
        print('')