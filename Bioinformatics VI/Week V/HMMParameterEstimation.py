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
                if val == 0:
                    val_str = '0'
                elif val == int(val):
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


if __name__ == "__main__":

    tmp = sys.stdin.read().splitlines()
    
    x = tmp[0]
    alphabet = tmp[2].split()
    path = tmp[4]
    all_states = tmp[6].split()
    transition_matrix, emission_matrix = HMMParameterEstimation(x, path, alphabet, all_states)
    print_matrices(transition_matrix, emission_matrix)