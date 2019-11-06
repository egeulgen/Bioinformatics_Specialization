def HammingDistance(p, q):
	mm = [p[i] != q[i] for i in range(len(p))]
	return sum(mm)

def Neighbors(Pattern, d):
	if d == 0:
		return [Pattern]
	if len(Pattern) == 1:
		return ['A', 'C', 'G', 'T'] 
	Neighborhood = []
	SuffixNeighbors = Neighbors(Pattern[1:], d)
	for Text in SuffixNeighbors:
		if HammingDistance(Pattern[1:], Text) < d:
			for nuc in ['A', 'C', 'G', 'T']:
				Neighborhood.append(nuc + Text)
		else:
			Neighborhood.append(Pattern[0] + Text)
	return Neighborhood

def ApproximatePatternCount(Text, Pattern, d):
	count = 0
	k = len(Pattern)
	L = len(Text)
	for i in range(L - k + 1):
		if HammingDistance(Text[i:i+k], Pattern) <= d:
			count += 1
	return count

def MotifEnumeration(DNA_list, k, d):
	Patterns = []
	DNA = DNA_list[0]
	del(DNA_list[0])
	for i in range(len(DNA) - k + 1):
		Pattern = DNA[i:i+k]
		Neighborhood = Neighbors(Pattern, d)
		for kmer in Neighborhood:
			count = 0
			for other in DNA_list:
				count += ApproximatePatternCount(other, kmer, d) != 0
			if count == len(DNA_list):
				Patterns.append(kmer)
	Patterns = list(set(Patterns))
	return Patterns

DNA_list = []
file = open('dataset_156_8.txt')
for i, line in enumerate(file):
	if i == 0:
		k, d = map(int, line.rstrip().split(' '))
	else:
		DNA_list.append(line.rstrip())

result = MotifEnumeration(DNA_list, k, d)
' '.join(result)
