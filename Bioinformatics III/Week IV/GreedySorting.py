def kSortingReversal(P, k):
    increment = 0
    j = k
    while P[j] != k + 1 and P[j] != -(k + 1):
        j += 1
    P[k:j+1] = list(map(lambda x: -x, P[k:j+1][::-1]))
    return P

def GreedySorting(P):
    reversals = []
    for k in range(len(P)):
        while P[k] != k + 1:
            P = kSortingReversal(P, k)
            reversals.append(list(P))
    return reversals

if __name__ == "__main__":
    P = input().rstrip()
    P = P[1:-1].split(' ')
    for i in range(len(P)):
        P[i] = int(P[i])
    result = GreedySorting(P)
    print(len(result))
    for r in result:
        print('(' + ' '.join(('+' if i > 0 else '') + str(i) for i in r) + ')')