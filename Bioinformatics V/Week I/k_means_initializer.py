import sys
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