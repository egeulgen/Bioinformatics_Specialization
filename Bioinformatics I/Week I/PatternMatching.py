def PatternMatching(Pattern, Genome):
	i = 0
	k = len(Pattern)
	L = len(Genome)
	start_idx = []
	while i < L - 1:
		if Genome[i:i+k] == Pattern:
			start_idx.append(i)
		i += 1
	return start_idx


Pattern = 'CTTGATCAT'
file = open('./Vibrio_cholerae.txt')
Genome = file.read()
Genome = Genome.rstrip()

res = PatternMatching(Pattern, Genome)
' '.join(map(str, res))