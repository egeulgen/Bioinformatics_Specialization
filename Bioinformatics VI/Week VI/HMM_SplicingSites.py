import graphviz
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint 
from collections import Counter

######## Set-up
alphabet = ['A', 'C', 'G', 'T']
states = ('exon', 'donor1', 'donor2', 'intron', 'acceptor1', 'acceptor2')

start_probability = {'exon': 0.50, 'donor1': 0.00, 'donor2': 0.00, 'intron': 0.50, 'acceptor1': 0.00, 'acceptor2': 0.00}

state_space = pd.Series(start_probability, index=states, name='states')

transition_probability = {
   'exon'      : {'exon': 0.90, 'donor1': 0.10, 'donor2': 0.00, 'intron': 0.00, 'acceptor1': 0.00, 'acceptor2': 0.00},
   'donor1'    : {'exon': 0.00, 'donor1': 0.00, 'donor2': 1.00, 'intron': 0.00, 'acceptor1': 0.00, 'acceptor2': 0.00},
   'donor2'    : {'exon': 0.00, 'donor1': 0.00, 'donor2': 0.00, 'intron': 1.00, 'acceptor1': 0.00, 'acceptor2': 0.00},
   'intron'    : {'exon': 0.00, 'donor1': 0.00, 'donor2': 0.00, 'intron': 0.90, 'acceptor1': 0.10, 'acceptor2': 0.00},
   'acceptor1' : {'exon': 0.00, 'donor1': 0.00, 'donor2': 0.00, 'intron': 0.00, 'acceptor1': 0.00, 'acceptor2': 1.00},
   'acceptor2' : {'exon': 1.00, 'donor1': 0.00, 'donor2': 0.00, 'intron': 0.00, 'acceptor1': 0.00, 'acceptor2': 0.00}
   }
transition_df = pd.DataFrame(transition_probability)

emission_probability = {
   'exon'      : {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
   'donor1'    : {'A': 0.05, 'C': 0.00, 'G': 0.95, 'T': 0.00},
   'donor2'    : {'A': 0.00, 'C': 0.05, 'G': 0.00, 'T': 0.95},
   'intron'    : {'A': 0.40, 'C': 0.10, 'G': 0.10, 'T': 0.40},
   'acceptor1' : {'A': 0.95, 'C': 0.00, 'G': 0.05, 'T': 0.00},
   'acceptor2' : {'A': 0.05, 'C': 0.00, 'G': 0.95, 'T': 0.00}
   }

emission_df = pd.DataFrame(emission_probability)

observations = ('A','T','G','G','C','C','C','G','A','A','C','C','A','A','G','C','A','G','A','C','T','G','C','G','C','G','C',
                'A','A','G','T','C','A','A','C','G','G','G','T','G','G','C','A','A','G','G','C','G','C','C','G','C','G','C',
                'A','A','G','C','A','G','C','T','G','G','C','C','A','C','C','A','A','G','G','T','G','G','C','T','C','G','C',
                'A','A','G','A','G','C','G','C','A','C','C','T','G','C','C','A','C','T','G','G','C','G','G','C','G','T','G',
                'A','A','G','A','A','G','C','C','G','C','A','C','C','G','C','T','A','C','C','G','G','C','C','C','G','G','C',
                'A','C','G','G','T','G','G','C','G','C','T','T','C','G','C','G','A','G','A','T','C','C','G','C','C','G','C',
                'T','A','C','C','A','G','A','A','G','T','C','C','A','C','T','G','A','G','C','T','G','C','T','A','A','T','C',
                'C','G','C','A','A','G','T','T','G','C','C','C','T','T','C','C','A','G','C','G','G','C','T','G','A','T','G',
                'C','G','C','G','A','G','A','T','C','G','C','T','C','A','G','G','A','C','T','T','T','A','A','G','A','C','C',
                'G','A','C','C','T','G','C','G','C','T','T','C','C','A','G','A','G','C','T','C','G','G','C','C','G','T','G',
                'A','T','G','G','C','G','C','T','G','C','A','G','G','A','G','G','C','G','T','G','C','G','A','G','T','C','T',
                'T','A','C','C','T','G','G','T','G','G','G','G','C','T','G','T','T','T','G','A','G','G','A','C','A','C','C',
                'A','A','C','C','T','G','T','G','T','G','T','C','A','T','C','C','A','T','G','C','C','A','A','A','C','G','G',
                'G','T','C','A','C','C','A','T','C','A','T','G','C','C','T','A','A','G','G','A','C','A','T','C','C','A','G',
                'C','T','G','G','C','A','C','G','C','C','G','T','A','T','C','C','G','C','G','G','G','G','A','G','C','G','G',
                'G','C','C','T','A','G','G','A','G','G','G','C','T','A','T','C','T','C','G','C','C','A','C','C','T','G','A',
                'G','A','G','G','T','T','G','C','G','C','A','A','C','G','T','T','C','A','C','C','C','C','A','A','A','G','G',
                'C','T','C','T','T','T','T','A','A','G','A','G','C','C','A','C','C','C','A','C','C','T')

######## Create HMM diagram
# create a function that maps transition probability dataframe 
# to markov edges and weights

def _get_markov_edges(transition_df):
    edges = {}
    for col in transition_df.columns:
        for idx in transition_df.index:
            edges[(idx,col)] = transition_df.loc[idx,col]
    return edges

tr_edges_wts = _get_markov_edges(transition_df)
tr_edges_wts = {key: val for key, val in tr_edges_wts.items() if val != 0}

em_edges_wts = _get_markov_edges(emission_df)
em_edges_wts = {key: val for key, val in em_edges_wts.items() if val != 0}
# pprint(em_edges_wts)

## create graph object
G = nx.MultiDiGraph()

## nodes correspond to states and emitted symbols
G.add_nodes_from(['start'])
G.add_nodes_from(states, color = 'black', style = 'filled', fillcolor = 'gray60', shape = 'rectangle')
G.add_nodes_from(alphabet, color = 'black', style = 'filled', fillcolor = 'gray90')

## edges represent transition probabilities and emission probabilities

# add transition edges
G.add_edge('start', 'exon', weight=0.5, label='')
G.add_edge('start', 'intron', weight=0.5, label='')
for k, v in tr_edges_wts.items():
    tmp_origin, tmp_destination = k[1], k[0]
    G.add_edge(tmp_origin, tmp_destination, weight=v, label='')

# add emission edges
for k, v in em_edges_wts.items():
    tmp_origin, tmp_destination = k[1], k[0]
    G.add_edge(tmp_origin, tmp_destination, weight=v, label='', style = 'dashed')

pos = nx.drawing.nx_pydot.graphviz_layout(G, prog='dot')


nx.drawing.nx_pydot.write_dot(G, 'SplicingSites_HMM.dot')

# python HMM_SplicingSites.py && dot -Tpng SplicingSites_HMM.dot > SplicingSites_HMM.png

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
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])
 
prob, most_likely_hidden_path = viterbi(observations, states, start_probability, transition_probability, emission_probability)

print(most_likely_hidden_path)
print(Counter(most_likely_hidden_path))