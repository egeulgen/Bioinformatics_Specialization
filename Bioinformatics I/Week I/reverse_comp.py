def reverse_comp(Pattern):
	return Pattern[::-1].translate(Pattern.maketrans('ATCG', 'TAGC'))