def Overlap(Patterns):
	adj_list = []
	for i, pattern in enumerate(Patterns):
		remaining = [pat for j, pat in enumerate(Patterns) if j != i]
		temp = []
		for pattern2 in remaining:
			if pattern[1:] == pattern2[:-1]:
				temp.append(pattern2)
		if len(temp) != 0:
			temp = pattern + ' -> ' + ', '.join(temp)
			adj_list.append(temp)
	return adj_list



if __name__ == "__main__":
	import sys
	DNA_list = sys.stdin.read().splitlines()
	res = Overlap(DNA_list)
	for r in res:
		print r
