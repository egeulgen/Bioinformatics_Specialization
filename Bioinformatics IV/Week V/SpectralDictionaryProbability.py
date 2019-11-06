import sys

mass_file=open('integer_mass_table.txt')
masses = []
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    masses.append(int(mass))

# masses = [4, 5]

def SpectralDictionaryProbability(spectral_vector, threshold, max_score):
    m = len(spectral_vector)

    Prob = {}
    Prob[0] = {}
    Prob[0][0] = 1

    for t in range(1, max_score + 1):
        Prob[0][t] = 0

    for i in range(1, m + 1):
        Prob[i] = {}
        for t in range(max_score + 1):
            Prob[i][t] = 0
            for a in masses:
                if (i - a) >= 0 and (t - spectral_vector[i - 1]) >= 0 and (t - spectral_vector[i - 1]) <= max_score:
                    Prob[i][t] += Prob[i - a][t - spectral_vector[i - 1]]
            Prob[i][t] /= 20

    final_Prob = 0
    for t in range(threshold, max_score + 1):
        final_Prob += Prob[m][t]

    return final_Prob

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    spectral_vector = [int(x) for x in tmp[0].rstrip().split(' ')]
    threshold = int(tmp[1])
    max_score = int(tmp[2])

    print(SpectralDictionaryProbability(spectral_vector, threshold, max_score))