def PatternCount(Text, Pattern):
	l = len(Pattern)
	L = len(Text)
	count = 0
	for i in range(L - l + 1):
		if Text[i:i+l] == Pattern:
			count += 1
	return count