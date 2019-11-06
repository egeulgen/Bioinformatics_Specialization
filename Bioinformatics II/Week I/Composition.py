def Composition(Text, k):
	comp = []
	for i in range(len(Text) - k + 1):
		comp.append(Text[i:i+k])
	comp.sort()
	return comp

if __name__ == "__main__":
    k = input().rstrip()
    Text = input().rstrip()
  
    ans = Composition(Text, k)
    for a in ans:
        print(a)