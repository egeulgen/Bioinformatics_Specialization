file = open('BLOSUM62.txt')
file = file.read().split('\n')
keys = file[0].split()
BLOSUM62 = {}
for i in range(1, len(file)):
    temp = file[i].split()
    key2 = temp[0]
    for j, key in enumerate(keys):
        if not key in BLOSUM62:
            BLOSUM62[key] = {key2: int(temp[j + 1])}
        else:
            BLOSUM62[key][key2] = int(temp[j + 1])

def Score(v, w):
	score = 0
	for i in range(len(v)):
		if v[i] == '-' or w[i] == '-':
			score -= 5
		else:
			score += BLOSUM62[v[i]][w[i]]
			gap_init = True
	return score

if __name__ == "__main__":
    v = input().rstrip()
    w = input().rstrip()
    print(Score(v, w))