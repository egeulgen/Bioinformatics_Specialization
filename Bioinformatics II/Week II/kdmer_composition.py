def kdmerComposition(Text, k, d):
	kmer_comp = []
	for i in range(len(Text) - k + 1):
		kmer1 = Text[i : i + k]
		j = i + k + d
		if j + k <= len(Text):
			kmer2 = Text[j:j+k]
			kmer_comp.append('(' + kmer1 + '|' + kmer2 + ')')
	kmer_comp.sort()
	return kmer_comp