def Random(prob_list):
	from random import random
	tot = sum(prob_list)
	massDist = map(lambda x: x/tot, prob_list)
	randRoll = random()
	cum = 0
	result = 1
	for mass in massDist:
		cum += mass
		if randRoll < cum:
			return result
		result += 1