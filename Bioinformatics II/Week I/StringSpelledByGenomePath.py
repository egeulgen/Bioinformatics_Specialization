def StringSpelledByGenomePath(DNA_list):
	string = DNA_list[0]
	del DNA_list[0]
	DNA_list
	for i, dna in enumerate(DNA_list):
		string += dna[-1]
	return string


if __name__ == "__main__":
	import sys
	DNA_list = sys.stdin.read().splitlines()
	print StringSpelledByGenomePath(DNA_list)
