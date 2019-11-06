import sys

def ProbabilityOutcomeGivenPath(x, hidden_path, emission_matrix):
    ''' Probability of an Outcome Given a Hidden Path Problem
    Input: A string x, followed by the alphabet from which x was constructed, followed by
     a hidden path π, followed by the states States and emission matrix Emission of 
     an HMM(Σ, States, Transition, Emission).
    Output: The conditional probability Pr(x|π) that x will be emitted given that the HMM
     follows the hidden path π.

    Note: You may assume that transitions from the initial state occur with equal probability.
    '''

    emission_prob = 1
    # Calculate ∏ (i: 1 -> n) emission𝜋𝑖(𝑥𝑖)
    for i in range(len(x)):
        emission_prob *= emission_matrix[hidden_path[i]][x[i]]

    return emission_prob

if __name__ == "__main__":

    tmp = sys.stdin.read().splitlines()

    x = tmp[0] # the emitted string
    alphabet = tmp[2].split(' ')
    hidden_path = tmp[4]
    states = tmp[6]

    col_syms = tmp[8].split('\t')[1:]
    emission_matrix = {}
    for i in range(9, len(tmp)):
        current_line = tmp[i].rstrip().split('\t')
        row_sym = current_line[0]
        emission_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            emission_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    print(ProbabilityOutcomeGivenPath(x, hidden_path, emission_matrix))