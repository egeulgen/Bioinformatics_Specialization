def HammingDistance(p, q):
	mm = [p[i] != q[i] for i in range(len(p))]
	return sum(mm)

def reverse_comp(Pattern):
	nuc_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	res = ''
	for n in Pattern[::-1]:
		res += nuc_dict[n]
	return res

def Neighbors(Pattern, d):
	if d == 0:
		return [Pattern]
	if len(Pattern) == 1:
		return ['A', 'C', 'G', 'T'] 
	Neighborhood = set()
	SuffixNeighbors = Neighbors(Pattern[1:], d)
	for Text in SuffixNeighbors:
		if HammingDistance(Pattern[1:], Text) < d:
			for nuc in ['A', 'C', 'G', 'T']:
				Neighborhood.add(nuc + Text)
		else:
			Neighborhood.add(Pattern[0] + Text)
	return Neighborhood

def FrequentWordsWithMismatchesAndReverseComplements(Text, k, d):
	pattern_dict = {}
	max_val = -1
	for i in range(len(Text) - k + 1):
		Pattern = Text[i:i+k]
		Neighborhood = Neighbors(Pattern, d)
		for ApproximatePattern in Neighborhood:
			revCompApproximatePattern = reverse_comp(ApproximatePattern)
			if ApproximatePattern in pattern_dict.keys():
				pattern_dict[ApproximatePattern] += 1
				if pattern_dict[ApproximatePattern] > max_val:
					max_val = pattern_dict[ApproximatePattern]
			else:
				pattern_dict[ApproximatePattern] = 1
				if pattern_dict[ApproximatePattern] > max_val:
					max_val = pattern_dict[ApproximatePattern]
			if revCompApproximatePattern in pattern_dict.keys():
				pattern_dict[revCompApproximatePattern] += 1
				if pattern_dict[revCompApproximatePattern] > max_val:
					max_val = pattern_dict[revCompApproximatePattern]
			else:
				pattern_dict[revCompApproximatePattern] = 1
				if pattern_dict[revCompApproximatePattern] > max_val:
					max_val = pattern_dict[revCompApproximatePattern]
	FrequentPatterns = []
	for key, value in pattern_dict.iteritems():
		if value == max_val:
				FrequentPatterns.append(key)
	return FrequentPatterns
