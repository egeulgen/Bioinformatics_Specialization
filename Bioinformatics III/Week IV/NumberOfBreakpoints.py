def NumberOfBreakpoints(P):
    P = [0] + P + [len(P) + 1]
    num_bps = 0
    for i in range(len(P) - 1):
        if P[i + 1] != P[i] + 1:
            num_bps +=1
    return num_bps

if __name__ == "__main__":
    P = input().rstrip()
    P = P[1:-1].split(' ')
    for i in range(len(P)):
        P[i] = int(P[i])
    print(NumberOfBreakpoints(P))