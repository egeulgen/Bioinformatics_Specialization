## Q4
s = [0, 0, 1, 1, 0, 0, 1, 0]
t = [1, 1, 0, 0, 1, 1, 1, 1]
n = len(t) 

diff_S_t = 0
diff_t = 0
## For individuals (i,j) if t[i] != t[j]
# and if s[i] != s[j]
# increase the total by 1
for i in range(n):
    for j in [x for x in range(n) if x != i]:
        if t[i] != t[j]:
            diff_t += 1
            if s[i] != s[j]:
                diff_S_t += 1

difference = diff_S_t / diff_t
round(difference, 3)

## Q5
import itertools
lst = list(itertools.product([0, 1], repeat = 5))
tmp = [0, 1, 1, 0, 0]
indices = [idx for idx in range(len(tmp)) if tmp[idx] == 1]

count = 0
for x in lst:
    x_indices = [idx for idx in range(len(x)) if x[idx] == 1]
    if set(x_indices).issubset(indices) or set(indices).issubset(x_indices) or not any(idx in x_indices for idx in indices):
        print(x)
        count += 1


0, 1, 1, 0, 0

1, 0, 0, 1, 1

(0, 0, 0, 0, 1)
(0, 0, 0, 1, 0)
(0, 0, 0, 1, 1)
(0, 0, 1, 0, 0)
(0, 0, 1, 0, 1)
(0, 0, 1, 1, 0)
(0, 0, 1, 1, 1)
(0, 1, 0, 0, 0)
(0, 1, 0, 0, 1)
(0, 1, 0, 1, 0)
(0, 1, 0, 1, 1)
(0, 1, 1, 0, 1)
(0, 1, 1, 1, 0)
(0, 1, 1, 1, 1)
(1, 0, 0, 0, 0)
(1, 0, 0, 0, 1)
(1, 0, 0, 1, 0)
(1, 0, 0, 1, 1)
(1, 0, 1, 0, 0)
(1, 0, 1, 0, 1)
(1, 0, 1, 1, 0)
(1, 0, 1, 1, 1)
(1, 1, 0, 0, 0)
(1, 1, 0, 0, 1)
(1, 1, 0, 1, 0)
(1, 1, 0, 1, 1)
(1, 1, 1, 0, 0)
(1, 1, 1, 0, 1)
(1, 1, 1, 1, 0)
(1, 1, 1, 1, 1)

## Q3

# Imagine an isolated population in which each adult female has a distinct mitochondrial genome. In each generation, every adult female has two children (with a 50% chance of being male or female). After each generation, we will assume that all the adults die out, and all the children become adults.

# After six generations, what is the expected percentage of mitochondria from the original population of females that will still exist in the population’s children? Express your answer as a decimal between 0 and 1, rounded to three decimal places.

# Note: after one generation, there will be 100% of the mitochondria from the original population present in the population’s children since male children receive the mitochondria from their mothers (but do not pass them on to their own children.)

# 0: 100
# 1: 100 - 200 * 0.5 = 100 F
# 2: 200 - 200 M 200 F
# 3: 400 - 400 M 400 F 
# 4: 800 - 800 M 800 F