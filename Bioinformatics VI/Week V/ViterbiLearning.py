import sys

def print_matrices(*argv, delim = "\t", separator = "--------"):
    ''' Function for printing multiple matrices
    Prints each matrix (stored as a dictionary) in 
    tab-delimited format (default). Seperates the 
    matrices with '--------' (default).
    '''

    for idx, matrix in enumerate(argv):

        row_labels = list(matrix.keys())
        col_labels = list(matrix[row_labels[0]].keys())
        if idx == 0:
            to_print = delim + delim.join(col_labels) + '\n'
            # to_print = delim + delim.join(col_labels) + '\t\n' # fix for required format
        else:
            to_print = delim + delim.join(col_labels) + '\n'

        for r_label in row_labels:
            tmp = [r_label]
            for c_label in col_labels:
                val = matrix[r_label][c_label]
                if val == int(val):
                    val_str = '{:.1f}'.format(val)
                else:
                    val_str = '{:.3f}'.format(val).rstrip('0')
                tmp.append(val_str)
            to_print += delim.join(tmp)
            if r_label != row_labels[-1]:
                to_print += '\n'

        print(to_print)
        if idx != len(argv) - 1:
            print(separator)

    return None

def HMMParameterEstimation(x, path, alphabet, all_states):
    ''' The HMM Parameter Estimation Problem
    Input: A string x of symbols emitted from an HMM, followed by the HMM's alphabet Σ,
     followed by a path π, followed by the collection of states of the HMM.
    Output: A transition matrix Transition followed by an emission matrix Emission that maximize
     Pr(x, π) over all possible transition and emission matrices.
    '''

    transitions = {}
    for i in range(1, len(path)):
        current = (path[i - 1], path[i])
        if current in transitions.keys():
            transitions[current] += 1
        else:
            transitions[current] = 1

    transition_matrix = {}
    for state1 in all_states:

        transition_matrix[state1] = {}

        total_transitions = 0
        for state2 in all_states:
            if (state1, state2) in transitions.keys():
                total_transitions += transitions[(state1, state2)]

        for state2 in all_states:
            # assume uniform transition probability 
            # if no transition from state 1 was observed
            if total_transitions == 0:
                transition_matrix[state1][state2] = 1 / len(all_states)
            else:
                if (state1, state2) in transitions.keys():
                    transition_matrix[state1][state2] = transitions[(state1, state2)] / total_transitions
                else:
                    transition_matrix[state1][state2] = 0

    
    emissions = {}
    for state, symbol in zip(path, x):
        current = (state, symbol)
        if current in emissions.keys():
            emissions[current] += 1
        else:
            emissions[current] = 1

    emission_matrix = {}
    for state in all_states:
        emission_matrix[state] = {}

        total_emissions = 0
        for symbol in alphabet:
            if (state, symbol) in emissions.keys():
                total_emissions += emissions[(state, symbol)]

        for symbol in alphabet:
            # assume uniform emission probability 
            # if state was not observed in path
            if total_emissions == 0:
                emission_matrix[state][symbol] = 1 / len(alphabet)
            else:
                if (state, symbol) in emissions.keys():
                    emission_matrix[state][symbol] = emissions[(state, symbol)] / total_emissions
                else:
                    emission_matrix[state][symbol] = 0

    return transition_matrix, emission_matrix

def Viterbi(x, all_states, transition_matrix, emission_matrix):
    ''' Implementation of the Viterbi algorithm for solving the Decoding Problem
    Input: A string x, followed by the alphabet from which x was constructed,
     followed by the states States, transition matrix Transition, and emission matrix
     Emission of an HMM (Σ, States, Transition, Emission).
    Output: A path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π.

    Note: You may assume that transitions from the initial state occur with equal probability.
    '''
    init_transition_prob = 1 / len(all_states)

    ## calculate all scores 
    backtrace = {}
    Score_dict = {}
    for i in range(len(x)):
        backtrace[i] = {}
        for current_state in all_states:
            if current_state not in Score_dict.keys():
                Score_dict[current_state] = {}
            ## if the leftmost column, initialize the recurrence
            # (every node in the leftmost column is connected to source)
            if i == 0:
                # Score[source] is 1
                Score_dict[current_state][i] = 1 * init_transition_prob * emission_matrix[current_state][x[i]]
            
            # 𝑠𝑘,𝑖 = max𝑎𝑙𝑙 𝑠𝑡𝑎𝑡𝑒𝑠 𝑙{𝑠𝑙,𝑖−1⋅𝑡𝑟𝑎𝑛𝑠𝑖𝑡𝑖𝑜𝑛𝑙,𝑘⋅𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑘(𝑥𝑖)}
            else:
                Score_dict[current_state][i] = -1e6
                for state in all_states:
                    tmp_score = Score_dict[state][i - 1] * transition_matrix[state][current_state] * emission_matrix[current_state][x[i]]
                    if tmp_score > Score_dict[current_state][i]:
                        Score_dict[current_state][i] = tmp_score
                        backtrace[i][current_state] = state
    
    ## Backtrace the maximum scoring path                
    max_score_state = max(Score_dict.keys(), key=lambda state: Score_dict[state][len(x) - 1])
    most_probable_path = max_score_state

    current_state = max_score_state
    for i in range(len(x) - 1, 0, -1):
        prev_state = backtrace[i][current_state]
        most_probable_path = prev_state + most_probable_path
        current_state = prev_state

    return most_probable_path


def Viterbi_Learning(x, init_transition_matrix, init_emission_matrix, alphabet, all_states, max_iterations):
    ''' Implement Viterbi learning for estimating the parameters of an HMM.
    Input: A number of iterations j, followed by a string x of symbols emitted by an HMM,
     followed by the HMM's alphabet Σ, followed by the HMM's states, followed by initial transition
     and emission matrices for the HMM.
    Output: Emission and transition matrices resulting from applying Viterbi learning for j iterations.
    '''

    transition_matrix = init_transition_matrix
    emission_matrix = init_emission_matrix

    for iteration in range(max_iterations):

        # Step 1: Determine path using current parameters
        path = Viterbi(x, all_states, transition_matrix, emission_matrix)

        # Step 2: Determine new parameters using path
        transition_matrix, emission_matrix = HMMParameterEstimation(x, path, alphabet, all_states)

    return transition_matrix, emission_matrix


if __name__ == "__main__":

    tmp = sys.stdin.read().splitlines()
    
    j = tmp[0]
    x = tmp[2]
    alphabet = tmp[4].split()
    all_states = tmp[6].split()

    init_transition_matrix = {}
    init_emission_matrix = {}

    # initial transition matrix
    col_syms = tmp[8].split('\t')[1:]
    transition_end = 8 + len(all_states)

    for i in range(9, transition_end + 1):
        current_line = tmp[i].rstrip().split('\t')
        row_sym = current_line[0]
        init_transition_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            init_transition_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    # emission matrix
    col_syms = tmp[transition_end + 2].split('\t')[1:]

    for i in range(transition_end + 3, len(tmp)):
        current_line = tmp[i].rstrip().split('\t')
        row_sym = current_line[0]
        init_emission_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            init_emission_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])


    transition_matrix, emission_matrix = Viterbi_Learning(x, init_transition_matrix, init_emission_matrix, alphabet, all_states, j)

    print_matrices(transition_matrix, emission_matrix)