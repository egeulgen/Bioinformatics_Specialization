import pandas as pd

def Euclidean_distance(PointA, PointB):
    if len(PointA) != len(PointB):
        raise ValueError('The dimensions are not the same!')
    dist = 0
    for i in range(len(PointA)):
        dist += ((PointA[i] - PointB[i]) ** 2)
    dist **= 1/2
    return dist

def HierarchicalClustering(distance_matrix, k, agg_method = 'average'):
    clusters = [[i] for i in range(len(distance_matrix))]

    while len(clusters) != 1:

        ## Find the two closest clusters
        min_dist = float('inf')
        for i in range(len(clusters) - 1):
            for j in range(i + 1, len(clusters)):
                if agg_method == 'average':
                    dist = 0
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            dist += distance_matrix[idx1][idx2]
                    dist /= (len(clusters[i]) * len(clusters[j]))
                elif agg_method == 'min':
                    dist = float('inf')
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            current = distance_matrix[idx1][idx2]
                            if current < dist:
                                dist = current
                elif agg_method == 'max':
                    dist = -1
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            current = distance_matrix[idx1][idx2]
                            if current > dist:
                                dist = current
                else:
                    raise Exception('Agglomeration method not implemented!')
                if dist < min_dist:
                    min_dist = dist
                    closest_idx1 = i
                    closest_idx2 = j

        ## Merge the two closeet clusters
        new_cluster = clusters[closest_idx1] + clusters[closest_idx2]
        clusters = [clu for clu in clusters if clu not in [clusters[closest_idx1], clusters[closest_idx2]]]
        clusters.append(new_cluster)
        if len(clusters) == k:
            break
    return clusters

if __name__ == "__main__":
    df = pd.read_csv('230genes_log_expression.txt', sep='\t', header=0, na_filter=False)
    exp_columns = [x for x in list(df.columns) if x.startswith('R')]

    Data = []
    for index, row in df.iterrows():
        Data.append(list(row[exp_columns]))

    distance_matrix = [[0 for j in range(len(Data))] for i in range(len(Data))]
    for i in range(len(Data)):
        for j in range(len(Data)):
            distance_matrix[i][j] = Euclidean_distance(Data[i], Data[j])

    new_clusters_list = HierarchicalClustering(distance_matrix, 6, 'average')
    for clu in new_clusters_list:
        print(' '.join([str(x + 1) for x in clu]))