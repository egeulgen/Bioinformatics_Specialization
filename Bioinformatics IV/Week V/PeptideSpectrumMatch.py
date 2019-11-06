import sys

mass_file=open('integer_mass_table.txt')
aa_table = {}
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    aa_table[aa] = int(mass)

aa_table['X'] = 4
aa_table['Z'] = 5


def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def PeptideVector(peptide):
    prefixMasses = []
    for i in range(len(peptide)):
        prefixMasses.append(sum(peptide[:i+1]))
    vector = [0] * prefixMasses[-1]
    for mass in prefixMasses:
        vector[mass - 1] = 1
    return vector

def PeptideIdentification(spectral_vector, proteome):
    max_score = -1e6
    mass_list = []
    for aa in proteome:
        mass_list.append(aa_table[aa])

    best_peptide = ''

    for i in range(len(mass_list)):
        k = 2
        while i + k < len(mass_list):
            peptide = mass_list[i:i+k]
            pep_vec = PeptideVector(peptide)
            if len(pep_vec) > len(spectral_vector):
                break
            if len(pep_vec) == len(spectral_vector):
                score = 0
                for idx in range(len(pep_vec)):
                    if pep_vec[idx] == 1:
                        score += spectral_vector[idx]
                if score > max_score:
                    max_score = score
                    best_peptide = proteome[i:i+k]
            k += 1
    return [best_peptide, max_score]

def PSMSearch(spectral_vectors, proteome, threshold):
    PSMSet = set()
    for vec in spectral_vectors:
        peptide, score = PeptideIdentification(vec, proteome)
        if score >= threshold:
            PSMSet.add(peptide)
    return PSMSet

if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()

    spectral_vectors = []
    idx = 0
    while is_number(tmp[idx][0]) or is_number(tmp[idx][:2]):
        vec = [int(x) for x in tmp[idx].rstrip().split(' ')]
        spectral_vectors.append(vec)
        idx += 1

    proteome = tmp[idx].rstrip()
    threshold = int(tmp[idx+1])

    result = PSMSearch(spectral_vectors, proteome, threshold)

    for res in result:
        print(res)
    
