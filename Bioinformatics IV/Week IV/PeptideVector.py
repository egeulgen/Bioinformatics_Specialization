import sys

mass_file=open('integer_mass_table.txt')
aa_table = {}
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    aa_table[aa] = int(mass)

aa_table['X'] = 4
aa_table['Z'] = 5

def PeptideVector(peptide):
    prefixMasses = []
    for i in range(len(peptide)):
        prefix = peptide[:i+1]
        mass = 0
        for aa in prefix:
            mass += aa_table[aa]
        prefixMasses.append(mass)

    vector = [0] * prefixMasses[-1]
    for mass in prefixMasses:
        vector[mass - 1] = 1
    return vector

if __name__ == "__main__":
    peptide = sys.stdin.read().rstrip()
    print(' '.join(str(x) for x in PeptideVector(peptide)))