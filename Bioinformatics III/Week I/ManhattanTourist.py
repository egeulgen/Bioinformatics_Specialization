def ManhattanTourist(n, m, Down, Right, Diag = None):
	S = [[0 for i in range(m + 1)] for j in range(n + 1)]
	for i in range(1, n + 1):
		S[i][0] = int(S[i - 1][0] + Down[i - 1][0])
	for j in range(1, m + 1):
		S[0][j] = S[0][j - 1] + Right[0][j - 1]
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			tmp1 = S[i - 1][j] + Down[i - 1][j]
			tmp2 = S[i][j - 1] + Right[i][j - 1]
			S[i][j] = max([tmp1, tmp2])
			if Diag != None:
				tmp3 = S[i - 1][j - 1] + Diag[i - 1][j - 1]
				S[i][j] = max([S[i][j], tmp3])
	for row in S:
		print(' '.join(map(str, row)))
	return S[n][m]


if __name__ == "__main__":
    n, m = input().rstrip().split(' ')
    n = int(n)
    m = int(m)
    line = input().rstrip()
    Down = []
    while line != '-':
    	temp = line.split(' ')
    	for i in range(len(temp)):
    		temp[i] = int(temp[i])
    	Down.append(temp)
    	line = input().rstrip()
    Right = []
    flag = True
    while flag:
    	try:
    		temp = input().split(' ')
    		for i in range(len(temp)):
    			temp[i] = int(temp[i])
	    	Right.append(temp)	
    	except EOFError:
    		flag = False
    print(ManhattanTourist(n, m, Down, Right))
    # Diag = [[5, 0, 2, 1], [8, 4, 3, 0], [10, 8, 9, 5], [5, 6, 4, 7]]
    # print(ManhattanTourist(n, m, Down, Right, Diag))