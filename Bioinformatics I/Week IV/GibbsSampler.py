from random import randint
from random import random

def GibbsSampler(Dna, k, t, N):
	Motifs = []
	for dna in Dna:
		idx = randint(0, len(dna) - k)
		Motifs.append(dna[idx:idx + k])
	BestMotifs = Motifs
	min_score = CalculateScore(BestMotifs)
	count_unchanged = 0
	for ITER in range(N):
		idx = randint(0, t - 1)
		profile = FormProfileWithPseudoCounts([motif for i, motif in enumerate(Motifs) if i != idx])
		Motifs[idx] = ProfileRandomlyGeneratedKmer(Dna[idx], profile)
		current_score = CalculateScore(Motifs)
		if current_score < min_score:
			BestMotifs = Motifs
			min_score = current_score
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

def ProfileRandomlyGeneratedKmer(Text, profile):
	L = len(Text)
	k = len(profile['A'])
	probs = []
	tot = profile['A'][0] + profile['C'][0] + profile['G'][0] + profile['T'][0]
	for i in range(L - k + 1):
		Motif = Text[i:i + k] 
		current_prob = 1.0
		for j, nuc in enumerate(Motif):
			current_prob *= float(profile[nuc][j]) / tot 
		probs.append(current_prob)
	selected_start = Random(probs)
	return Text[selected_start:selected_start + k]

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

def HammingDistance(p, q):
	mm = [p[i] != q[i] for i in range(len(p))]
	return sum(mm)

def CalculateScore(Motifs):
	k = len(Motifs[0])
	profile = FormProfileWithPseudoCounts(Motifs, 0)
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

def wrapper(Dna, k, t, N, nstart = 20):
	min_score = 1e6
	for i in range(nstart):
		res = GibbsSampler(Dna, k, t, N)
		current_score = CalculateScore(res)
		# print current_score
		if current_score < min_score:
			min_score = current_score
			result = res
	print min_score
	return result

# if __name__ == "__main__":
#     k, t, N = [int(a) for a in input().strip().split(" ")]
#     Dna = []
#     for _ in range(t):
#         Dna.append(input())
        
#     ans = wrapper(Dna, k, t, N)
#     for a in ans:
#         print(a)


Dna = []
file = open('DosR_1.txt')
for i, line in enumerate(file):
	if i == 0:
		k, t, N = map(int, line.rstrip().split(' '))
	else:
		Dna.append(line.rstrip())

res = wrapper(Dna, k, t, N)
for r in res:
	print r