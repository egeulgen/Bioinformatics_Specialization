import sys
from copy import deepcopy
from math import exp
from random import randint, random

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

def Random(prob_list):
    tot = sum(prob_list)
    massDist = map(lambda x: x/tot, prob_list)
    randRoll = random()
    cum = 0
    result = 0
    for mass in massDist:
        cum += mass
        if randRoll < cum:
            return result
        result += 1

def k_means_initializer(Data, k):
    Centers = [Data[randint(0, len(Data) - 1)]]
    while len(Centers) < k:
        prob_list = []
        available_Data = [x for x in Data if x not in Centers]
        for DataPoint in available_Data:
            prob_list.append(dist_from_centers(DataPoint, Centers) ** 2)
        Centers.append(available_Data[Random(prob_list)])
    return Centers

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

def soft_kmeans(Data, k, beta = 0.8):
    Centers = k_means_initializer(Data, k)
    while True:
        hidden_mat = Hidden_Matrix(Data, Centers, beta)
        n_centers = clu_to_center(hidden_mat, Data)

        tot_diff = 0
        for i in range(len(Centers)):
            for j in range(len(Centers[i])):
                tot_diff += abs(Centers[i][j] - n_centers[i][j])

        if tot_diff < 1e-5:
            break
        Centers = deepcopy(n_centers)
    return Centers

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    k, m = [int(x) for x in tmp[0].split(' ')] ## numbers of partitions, dimensions

    Data = []
    for i in range(1, len(tmp)):
        Data.append([float(d) for d in tmp[i].split(' ')])

    Centers = soft_kmeans(Data, k)
    for C in Centers:
        print(' '.join([str(x) for x in C]))