import sys

mass_file=open('integer_mass_table.txt')
masses = []
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    masses.append(int(mass))

# masses = [4, 5]

def SpectralDictionarySize(spectral_vector, threshold, max_score):
    m = len(spectral_vector)

    Size = {}
    Size[0] = {}
    Size[0][0] = 1

    for t in range(1, max_score + 1):
        Size[0][t] = 0

    for i in range(1, m + 1):
        Size[i] = {}
        for t in range(max_score + 1):
            Size[i][t] = 0
            for a in masses:
                if (i - a) >= 0 and (t - spectral_vector[i - 1]) >= 0 and (t - spectral_vector[i - 1]) <= max_score:
                    Size[i][t] += Size[i - a][t - spectral_vector[i - 1]]

    final_size = 0
    for t in range(threshold, max_score + 1):
        final_size += Size[m][t]

    return final_size

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    spectral_vector = [int(x) for x in tmp[0].rstrip().split(' ')]
    threshold = int(tmp[1])
    max_score = int(tmp[2])

    print(SpectralDictionarySize(spectral_vector, threshold, max_score))