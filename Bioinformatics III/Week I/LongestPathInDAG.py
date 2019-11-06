
def LongestPathInDAG(Graph, Start, End):
	nodes = []
	for edge in Graph:
		nodes.append(edge[0])
		nodes.append(edge[1])
	nodes = list(set(nodes))
	nodes.sort()
	i = 0
	node = nodes[0]
	while node != Start:
		i += 1
		node = nodes[i]
	scores = {Start: 0}
	Backtrace = {Start: -1}
	while node != End:
		i += 1
		node = nodes[i]
		weights = []
		from_nodes = []
		for edge in Graph:
			if edge[1] == node and edge[0] in scores.keys():
				if scores[edge[0]] != -1000:
					weights.append(scores[edge[0]] + edge[2])
					from_nodes.append(edge[0])
		if len(weights) != 0:
			scores[node] = max(weights)
			Backtrace[node] = [n for i, n in enumerate(from_nodes) if weights[i] == max(weights)]
		else:
			scores[node] = -1000
			Backtrace[node] = -1
	print(scores[End])
	return Backtrace

if __name__ == "__main__":
    Start = input().rstrip()
    End = input().rstrip()
    Graph = []
    flag = True
    while flag:
    	try:
    		temp = input().split(' -> ')
    		node = temp[0]
    		target, weight = temp[1].split(':')
    		target = target
    		weight = int(weight)
    		Graph.append([node, target, weight])
    	except EOFError:
    		flag = False
    print(Graph)
    result = LongestPathInDAG(Graph, Start, End)
    # print(result)
    longest_path = [str(End)]
    val = result[End]
    while val != -1:
    	longest_path.append(str(val[0]))
    	val = result[val[0]]
    print('->'.join(longest_path[::-1]))