sequence = ''
with open('Q09206.fasta') as f:
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		elif not line.startswith('>'):
			sequence += line.rstrip()
print(sequence)