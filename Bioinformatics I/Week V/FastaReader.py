def FastaReader(Path2File):
	sequences = {}
	file = open(Path2File, 'r')
	for i, line in enumerate(file):
		line = line.rstrip()
		if line.startswith('>'):
			if i != 0:
				sequences[seq_name] = seq
			seq_name = line[1:]
			seq = ''
		else:
			seq += line
	return sequences