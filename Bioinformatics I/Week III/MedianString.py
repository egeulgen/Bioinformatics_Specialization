def HammingDistance(p, q):
	mm = [p[i] != q[i] for i in range(len(p))]
	return sum(mm)

def NumberToPattern(Number, k):
	reverse = ['A', 'C', 'G', 'T']
	Pattern = ''
	for i in range(k - 1, -1, -1):
		current = Number // 4 ** i
		Pattern += reverse[current]
		Number %= 4 ** i
	return Pattern

def DistanceBetweenPatternAndStrings(Pattern, Dna_list):
	dist = 0
	k = len(Pattern)
	for dna in Dna_list:
		min_dist = len(dna)
		for i in range(len(dna) - k + 1):
			pat = dna[i:i + k]
			current_d = HammingDistance(pat, Pattern)
			if current_d < min_dist:
				min_dist = current_d
		dist += min_dist
	return dist

file = open('dataset_5164_1.txt')
for i, line in enumerate(file):
	if i == 0:
		Pattern = line.rstrip()
	else:
		Dna_list = line.rstrip().split(' ')

DistanceBetweenPatternAndStrings(Pattern, Dna_list)


def MedianString(Dna, k):
	distance = len(Dna[0]) * len(Dna)
	for i in range(4**k):
		Pattern = NumberToPattern(i, k)
		current_dist = DistanceBetweenPatternAndStrings(Pattern, Dna)
		if distance > current_dist:
			distance = current_dist
			Median = Pattern
	return Median


def MedianString2(Dna, k):
	distance = len(Dna[0]) * len(Dna)
	Medians = []
	for i in range(4**k):
		Pattern = NumberToPattern(i, k)
		current_dist = DistanceBetweenPatternAndStrings(Pattern, Dna)
		if distance > current_dist:
			distance = current_dist
			Medians = [Pattern]
		elif distance == current_dist:
			Medians.append(Pattern)
	return Medians


DNA_list = []
file = open('dataset_158_9.txt')
for i, line in enumerate(file):
	if i == 0:
		k = int(line.rstrip())
	else:
		DNA_list.append(line.rstrip())

result = MedianString(DNA_list, k)
' '.join(result)
