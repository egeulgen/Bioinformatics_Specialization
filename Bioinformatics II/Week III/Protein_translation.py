CODONS = {'AAA':'K','AAC':'N','AAG':'K','AAU':'N','ACA':'T','ACC':'T','ACG':'T','ACU':'T','AGA':'R','AGC':'S','AGG':'R','AGU':'S','AUA':'I','AUC':'I','AUG':'M','AUU':'I','CAA':'Q','CAC':'H','CAG':'Q','CAU':'H','CCA':'P','CCC':'P','CCG':'P','CCU':'P','CGA':'R','CGC':'R','CGG':'R','CGU':'R','CUA':'L','CUC':'L','CUG':'L','CUU':'L','GAA':'E','GAC':'D','GAG':'E','GAU':'D','GCA':'A','GCC':'A','GCG':'A','GCU':'A','GGA':'G','GGC':'G','GGG':'G','GGU':'G','GUA':'V','GUC':'V','GUG':'V','GUU':'V','UAA':'X','UAC':'Y','UAG':'X','UAU':'Y','UCA':'S','UCC':'S','UCG':'S','UCU':'S','UGA':'X','UGC':'C','UGG':'W','UGU':'C','UUA':'L','UUC':'F','UUG':'L','UUU':'F'}

def Translate(RNA):
	protein = ''
	for i in range(0, len(RNA) - 2, 3):
		codon = RNA[i:i + 3]
		aa = CODONS[codon]
		if aa != 'X':
			protein += aa
	return protein

def CountStrings(protein):
	res = 1
	for aa in protein:
		count_aa = 0
		for key, val in CODONS.items():
			if val == aa:
				count_aa += 1
		print(count_aa)
		res *= count_aa
	return res