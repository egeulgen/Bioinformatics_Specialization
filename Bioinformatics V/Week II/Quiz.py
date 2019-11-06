from math import exp

Data=[[2,8], [2,5], [6,9], [7,5], [5,2]]

Centers=[[3,5], [5,4]]


def Euclidean_distance(PointA, PointB):
    if len(PointA) != len(PointB):
        raise ValueError('The dimensions are not the same!')
    dist = 0
    for i in range(len(PointA)):
        dist += ((PointA[i] - PointB[i]) ** 2)
    dist **= 1/2
    return dist

def Hidden_Matrix(Data, Centers, beta = 1):
    hidden_mat = [[0 for j in range(len(Data))] for i in range(len(Centers))]
    for j in range(len(Data)):
        tot = 0
        for i in range(len(Centers)):
            tot += exp(-beta * Euclidean_distance(Centers[i], Data[j]))
        for i in range(len(Centers)):
            hidden_mat[i][j] = exp(-beta * Euclidean_distance(Centers[i], Data[j])) / tot
    return hidden_mat

def clu_to_center(hidden_mat, Data):
    k = len(hidden_mat)
    m = len(Data[0])
    n = len(Data)
    new_centers = [[0 for j in range(m)] for i in range(k)]
    for i in range(k):
        for j in range(m):
            product = 0
            for idx in range(n):
                product += Data[idx][j] * hidden_mat[i][idx]
            new_centers[i][j] = product / sum(hidden_mat[i])
    return new_centers


## Q2
round(Hidden_Matrix(Data, Centers)[0][4], 3)


## Q3
# Compute the weighted center of gravity corresponding to the second row of HiddenMatrix. Please enter your coordinates (x, y) in the form x y, rounded to three decimal places.
Data = [[2,8], [2,5], [6,9], [7,5], [5,2]]
HiddenMatrix = [[0.5, 0.3, 0.8, 0.4, 0.9], [0.5, 0.7, 0.2, 0.6, 0.1]]



print(str(round(clu_to_center(HiddenMatrix, Data)[1][0], 3)) + ' ' + str(round(clu_to_center(HiddenMatrix, Data)[1][1], 3)))

## Q5
#Below is a distance matrix D. If C1 = {i, l} and C2 = {j, k}, compute Davg(C1, C2).

distance_matrix = [[0, 20, 9, 11], [20, 0, 17, 11], [9, 17, 0, 8], [11, 11, 8, 0]]

clusters_1 = [0, 3]
clusters_2 = [1, 2]

dist = 0
for idx1 in clusters_1:
    for idx2 in clusters_2:
        dist += distance_matrix[idx1][idx2]

dist /= (len(clusters_1) * len(clusters_2))
print(dist)
