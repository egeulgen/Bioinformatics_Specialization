import sys

mass_file=open('integer_mass_table.txt')
mass_table = {}
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    mass_table[int(mass)] = aa

mass_table[4] = 'X'
mass_table[5] = 'Z'

def ConvertPeptideVector(vector):
    prefixMasses = []
    for i in range(len(vector)):
        if vector[i] == 1:
            prefixMasses.append(i + 1)

    peptide = mass_table[prefixMasses[0]]
    for i in range(1, len(prefixMasses)):
        mass = prefixMasses[i] - prefixMasses[i - 1]
        peptide += mass_table[mass]

    return peptide

if __name__ == "__main__":
    vector = [int(x) for x in sys.stdin.read().rstrip().split(' ')]
    
    print(ConvertPeptideVector(vector))