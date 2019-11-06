import sys
from copy import deepcopy

mass_file=open('integer_mass_table.txt')
mass_table = {}
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    mass_table[int(mass)] = aa

# mass_table[4] = 'X'
# mass_table[5] = 'Z'

def PeptideSequencing(spectral_vector):
    spectral_vector = [0] + spectral_vector

    adj_list = []
    for i in range(len(spectral_vector)):
        for j in range(i, len(spectral_vector)):
            if (j - i) in mass_table.keys():
                adj_list.append([i, j])

    adj_dict = {}
    for i in range(len(spectral_vector)):
        for j in range(i, len(spectral_vector)):
            if (j - i) in mass_table.keys():
                tmp = [i, mass_table[j - i]]
                if not j in adj_dict.keys():
                    adj_dict[j] = [tmp]
                else:
                    adj_dict[j].append(tmp)

    scores = {0: [0, '-']}
    for node in adj_dict.keys():
        scores[node] = [-1e6, '-']
        tmp = adj_dict[node]
        for x in tmp:
            if x[0] != 0:
                scores[x[0]] = [-1e6, '-']

    for node in adj_dict.keys():
        max_score = -1e6
        bold_edge = '-'
        for parent in adj_dict[node]:
            score = scores[parent[0]][0]
            if score > max_score:
                max_score = score
                bold_edge = parent
        scores[node] = [max_score + spectral_vector[node], bold_edge]

    node = list(scores.keys())[-1]
    peptide = ''
    while node != 0:
        peptide = scores[node][1][1] + peptide
        node = scores[node][1][0]

    return peptide

if __name__ == "__main__":
    spectral_vector = [int(x) for x in sys.stdin.read().rstrip().split(' ')]
    # print(spectral_vector)
    print(PeptideSequencing(spectral_vector))
