
def CalculateEntopy(Motifs):
	from math import log
	L = len(Motifs[0])
	props = []
	for i in range(L):
		counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
		for motif in Motifs:
			counts[motif[i]] += 1
		counts = counts.values()
		counts = map(lambda x : float(x)/sum(counts), counts)
		props += counts
	entropy = 0
	for p in props:
		if p != 0:
			entropy += -p * log(p, 2)
	return entropy

Motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]

def PlotInformationContent(Motifs):
	from math import log
	L = len(Motifs[0])
	all_props = []
	info_content = []
	for i in range(L):
		counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
		for motif in Motifs:
			counts[motif[i]] += 1
		counts = counts.values()
		props = map(lambda x : float(x)/sum(counts), counts)
		all_props.append(props)
		entropy = 0
		for p in props:
			if p != 0:
				entropy -= p * log(p, 2)
		info_content.append(2 - entropy)
	return (all_props, info_content)
