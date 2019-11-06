# The profile matrix assumes that the first row corresponds to A, the second corresponds to C,
# the third corresponds to G, and the fourth corresponds to T.
# You should represent the profile matrix as a dictionary whose keys are 'A', 'C', 'G', and 'T' and whose values are lists of floats
def ProfileMostProbableKmer(text, k, profile):
	max_prob = -1
	for i in range(len(text) - k + 1):
		Pattern = text[i:i + k]
		prob = profile[Pattern[0]][0]
		for j in range(1, len(Pattern)):
			nuc = Pattern[j]
			prob *= profile[nuc][j]
		if prob > max_prob:
			most_probable = Pattern
			max_prob = prob
	return most_probable


profile = {'A': 0, 'C': 0, 'G': 0, 'T': 0} 
keys = 'ACGT'
file = open('dataset_159_3.txt')
for i, line in enumerate(file):
	if i == 0:
		text = line.rstrip()
	elif i == 1:
		k = int(line.rstrip())
	else:
		temp = map(float, line.rstrip().split(' '))
		profile[keys[i - 2]] = temp

ProfileMostProbableKmer(text, k, profile)