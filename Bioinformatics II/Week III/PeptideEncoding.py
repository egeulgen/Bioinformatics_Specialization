CODONS = {'AAA':'K','AAC':'N','AAG':'K','AAU':'N','ACA':'T','ACC':'T','ACG':'T','ACU':'T','AGA':'R','AGC':'S','AGG':'R','AGU':'S','AUA':'I','AUC':'I','AUG':'M','AUU':'I','CAA':'Q','CAC':'H','CAG':'Q','CAU':'H','CCA':'P','CCC':'P','CCG':'P','CCU':'P','CGA':'R','CGC':'R','CGG':'R','CGU':'R','CUA':'L','CUC':'L','CUG':'L','CUU':'L','GAA':'E','GAC':'D','GAG':'E','GAU':'D','GCA':'A','GCC':'A','GCG':'A','GCU':'A','GGA':'G','GGC':'G','GGG':'G','GGU':'G','GUA':'V','GUC':'V','GUG':'V','GUU':'V','UAA':'X','UAC':'Y','UAG':'X','UAU':'Y','UCA':'S','UCC':'S','UCG':'S','UCU':'S','UGA':'X','UGC':'C','UGG':'W','UGU':'C','UUA':'L','UUC':'F','UUG':'L','UUU':'F'}

def reverse_comp(Pattern):
	return Pattern[::-1].translate(Pattern.maketrans('ATCG', 'TAGC'))

def Translate(RNA):
	protein = ''
	for i in range(0, len(RNA) - 2, 3):
		codon = RNA[i:i + 3]
		aa = CODONS[codon]
		if aa != 'X':
			protein += aa
	return protein

def PeptideEncoding(Text, Peptide):
	result = []
	## Check forward
	for i in range(0, len(Text) - 3 * len(Peptide)):
		encoding_DNA = Text[i:i + 3*len(Peptide)]
		encoding_RNA = list(encoding_DNA)
		for j, n in enumerate(encoding_RNA):
			if n == 'T':
				encoding_RNA[j] = 'U'
		if Translate(''.join(encoding_RNA)) == Peptide:
			result.append(encoding_DNA)
	## Check reverse
	rev_DNA = reverse_comp(Text)
	for i in range(0, len(rev_DNA) - 3 * len(Peptide)):
		encoding_DNA = rev_DNA[i:i + 3*len(Peptide)]
		encoding_RNA = list(encoding_DNA)
		for j, n in enumerate(encoding_RNA):
			if n == 'T':
				encoding_RNA[j] = 'U'
		if Translate(''.join(encoding_RNA)) == Peptide:
			result.append(reverse_comp(encoding_DNA))
	return result

if __name__ == "__main__":
    import sys
    Text, Peptide = sys.stdin.read().splitlines()
    res = PeptideEncoding(Text, Peptide)
    for r in res:
    	print(r)