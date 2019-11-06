def RandomizedMotifSearch(DNA_list, k, t):
	Motifs = []
	for dna in DNA_list:
		from random import randint
		idx = randint(0, len(dna) - k)
		Motifs.append(dna[idx:idx + k])
	BestMotifs = Motifs
	while True:
		profile = FormProfileWithPseudoCounts(Motifs)
		Motifs = []
		for dna in DNA_list:
			Motifs.append(ProfileMostProbableKmer(dna, k, profile))
		if CalculateScore(Motifs) < CalculateScore(BestMotifs):
			BestMotifs = Motifs
		else:
			return BestMotifs

def FormProfileWithPseudoCounts(TextList, pseudocount = 1):
	if type(TextList) != list:
		TextList = [TextList]
	t = len(TextList)
	k = len(TextList[0])
	profile = {'A': [pseudocount]*k, 'C': [pseudocount]*k, 'G': [pseudocount]*k, 'T': [pseudocount]*k}
	for i in range(k):
		for j in range(t):
			profile[TextList[j][i]][i] += 1
	return profile

def ProfileMostProbableKmer(text, k, profile):
	max_prob = -1
	for i in range(len(text) - k + 1):
		Pattern = text[i:i + k]
		prob = profile[Pattern[0]][0]
		for j in range(1, len(Pattern)):
			prob *= profile[Pattern[j]][j]
		if prob > max_prob:
			most_probable = Pattern
			max_prob = prob
	return most_probable

def HammingDistance(p, q):
	mm = [p[i] != q[i] for i in range(len(p))]
	return sum(mm)

def CalculateScore(Motifs):
	k = len(Motifs[0])
	profile = FormProfileWithPseudoCounts(Motifs)
	consensus = ''
	for i in range(k):
		most_freq = 0
		for nuc in ['A', 'C', 'G', 'T']:
			if profile[nuc][i] > most_freq:
				most_freq = profile[nuc][i]
				to_add = nuc
		consensus += to_add
	score = 0
	for motif in Motifs:
		score += HammingDistance(consensus, motif)
	return score

def wrapper(DNA_list, k, t, reps = 1000):
	best_score = 1e6
	for i in range(reps):
		res = RandomizedMotifSearch(DNA_list, k, t)
		current_score = CalculateScore(res)
		if current_score <= best_score:
			best_res = res
			best_score = current_score
	return best_res

# if __name__ == "__main__":
#     k,t = [int(a) for a in input().strip().split(" ")]
#     Dna = []
#     for _ in range(t):
#         Dna.append(input())
        
#     ans = wrapper(Dna, k, t)
#     for a in ans:
#         print(a)


DNA_list = []
file = open('dataset_161_5.txt')
for i, line in enumerate(file):
	if i == 0:
		k, t = map(int, line.rstrip().split(' '))
	else:
		DNA_list.append(line.rstrip())

res = wrapper(DNA_list, k, t)
for r in res:
	print r