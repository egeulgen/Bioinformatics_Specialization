from collections import Counter

states = ('A+', 'T+', 'C+', 'G+', 'A-', 'T-', 'G-', 'C-')
 
observations = []
with open('chr_22.txt') as f:
  while True:
    c = f.read(1)
    if not c:
      break 
    observations.append(c)
 
start_probability = {'A+': 0.125, 'T+': 0.125, 'G+': 0.125, 'C+': 0.125, 'A-': 0.125, 'T-': 0.125, 'G-': 0.125, 'C-': 0.125}
 
###################### VALUE TO CHANGE ############################    
##################### TRANSITION WEIGHT ########################### 
p = 0.1


transition_probability = {
   'A+' : {'A+': 0.180 *  (1-p), 'C+': 0.268 *  (1-p), 'G+': 0.430 *  (1-p), 'T+': 0.122 *  (1-p), 'A-': 0.25 * p, 'C-': 0.25 * p, 'G-': 0.25 * p, 'T-': 0.25 * p},
   'C+' : {'A+': 0.191 *  (1-p), 'C+': 0.299 *  (1-p), 'G+': 0.299 *  (1-p), 'T+': 0.211 *  (1-p), 'A-': 0.25 * p, 'C-': 0.25 * p, 'G-': 0.25 * p, 'T-': 0.25 * p},
   'G+' : {'A+': 0.161 *  (1-p), 'C+': 0.346 *  (1-p), 'G+': 0.373 *  (1-p), 'T+': 0.120 *  (1-p), 'A-': 0.25 * p, 'C-': 0.25 * p, 'G-': 0.25 * p, 'T-': 0.25 * p},
   'T+' : {'A+': 0.082 *  (1-p), 'C+': 0.357 *  (1-p), 'G+': 0.391 *  (1-p), 'T+': 0.170 *  (1-p), 'A-': 0.25 * p, 'C-': 0.25 * p, 'G-': 0.25 * p, 'T-': 0.25 * p},
   

   'A-' : {'A+': 0.25 * p, 'C+': 0.25 * p, 'G+': 0.25 * p, 'T+': 0.25 * p, 'A-': 0.300 *  (1-p), 'C-': 0.200 *  (1-p), 'G-': 0.290 *  (1-p), 'T-': 0.210 *  (1-p)},
   'C-' : {'A+': 0.25 * p, 'C+': 0.25 * p, 'G+': 0.25 * p, 'T+': 0.25 * p, 'A-': 0.319 *  (1-p), 'C-': 0.302 *  (1-p), 'G-': 0.081 *  (1-p), 'T-': 0.291 *  (1-p)},   
   'G-' : {'A+': 0.25 * p, 'C+': 0.25 * p, 'G+': 0.25 * p, 'T+': 0.25 * p, 'A-': 0.251 *  (1-p), 'C-': 0.251 *  (1-p), 'G-': 0.299 *  (1-p), 'T-': 0.199 *  (1-p)},
   'T-' : {'A+': 0.25 * p, 'C+': 0.25 * p, 'G+': 0.25 * p, 'T+': 0.25 * p, 'A-': 0.176 *  (1-p), 'C-': 0.242 *  (1-p), 'G-': 0.291 *  (1-p), 'T-': 0.291 *  (1-p)}

   }
 
emission_probability = {
   'A+' : {'A': 1.0, 'T': 0.0, 'G': 0.0, 'C': 0.0},
   'T+' : {'A': 0.0, 'T': 1.0, 'G': 0.0, 'C': 0.0},
   'G+' : {'A': 0.0, 'T': 0.0, 'G': 1.0, 'C': 0.0},
   'C+' : {'A': 0.0, 'T': 0.0, 'G': 0.0, 'C': 1.0},
   'A-' : {'A': 1.0, 'T': 0.0, 'G': 0.0, 'C': 0.0},
   'T-' : {'A': 0.0, 'T': 1.0, 'G': 0.0, 'C': 0.0},
   'G-' : {'A': 0.0, 'T': 0.0, 'G': 1.0, 'C': 0.0},
   'C-' : {'A': 0.0, 'T': 0.0, 'G': 0.0, 'C': 1.0}
   }

# Don't study this, it just prints a table of the steps.
def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)

######## Viterbi on this HMM
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
 
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
        path = newpath
    n = 0           # if only one element is observed max is sought in the initialization values
    if len(obs) != 1:
        n = t
    print_dptable(V)
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])
 
prob, most_likely_hidden_path = viterbi(observations, states, start_probability, transition_probability, emission_probability)

print(most_likely_hidden_path)
print(Counter(most_likely_hidden_path))