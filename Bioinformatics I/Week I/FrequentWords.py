def FrequentWords(Text, k):
    L = len(Text)
    pattern_dict = {}
    max_val = 0
    for i in range(L - k + 1):
        pattern = Text[i:i+k]
        if pattern in pattern_dict.keys():
			pattern_dict[pattern] += 1
        else:
            pattern_dict[pattern] = 1
        if pattern_dict[pattern] > max_val:
            max_val = pattern_dict[pattern]
	FrequentPatterns = []
    for key, value in pattern_dict.iteritems():
		if value == max_val:
			FrequentPatterns.append(key)
	return FrequentPatterns


def PatternToNumber(Pattern):
	indices = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	result = 0
	N = len(Pattern)
	for i in range(N):
		nuc = Pattern[i]
		result += indices[nuc]*4**(N - i - 1)
	return result

def NumberToPattern(Number, k):
	reverse = ['A', 'C', 'G', 'T']
	Pattern = ''
	for i in range(k - 1, -1, -1):
		current = Number // 4 ** i
		Pattern += reverse[current]
		Number %= 4 ** i
	return Pattern

def ComputingFrequencies(Text, k):
	L = len(Text)
	FrequencyArray = []
	for i in range(4**k):
		FrequencyArray.append(0)
	for i in range(L - k + 1):
		Pattern = Text[i:i+k]
		j = PatternToNumber(Pattern)
		FrequencyArray[j] += 1
	return FrequencyArray

# Text = 'AAATCTGGAGCCGTTAGGGCTTCGAGCTCTCTCTTCGAGAATTTCCCTGCAAAAGGTGGGCGCCAAGTTGTACGTTCTAAAATCTATCCGGCTTAGATCGCGACTTTGTCGACCCACAAGTTCCAGGTTTGATAGCCCAGGTTTTCGACAGTACTCTTCGCACCCGAACTAAACCGTCACCAATAGTCGTGTGGCTTCAAATTTACATAGGCTGTGAGAATATGCAAACTTTTGTTTGCCTATCCAAGTTCTTCCGATTGGGCGAGTGGCAGTTCGTATAGCGCTTTAAATTCTCTCCCATACGATTACTAGGATTGCGGAACTTATGATGCCGATAACATGCCCAACATGACCTAATGACGTTAGAATCTAACCGGTGTGCACAGGTTATCCAACGGGAAAATAACTCACACCGGGGTCGAACCACAGCGCAGGATGGGACAGTTCGCTCGTCCGGTAGGCTCGTCGTTAACCCCTACTAGGCGTAGGTCGTCGTCCTGCGACCCGTGGGGTGGGTCCCCTCAATGGAGGTTCTGGCGATAATTTTGGTGGCCCATGGTTTTCTCGTATCCACACGCTCTTGCCAAAGACTACGCTTTCATCAGTTGCGAAACGTGACGCTCAAGGTAAGCCGCAGCCGGCACGGGACCGCTTGTGAGGAGTAAAGGGTTTCTAAGGTAGATT'
# k = 5
# res = ComputingFrequencies(Text, k)
# ' '.join(map(str, res))

def FasterFrequentWords(Text, k):
	FrequentPatterns = []
	FrequencyArray = ComputingFrequencies(Text, k)
	maxCount = max(FrequencyArray)
	for i in range(len(FrequencyArray)):
		if FrequencyArray[i] == maxCount:
			Pattern = NumberToPattern(i, k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns