mass_file=open('integer_mass_table.txt')
mass_table = {}
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    mass_table[aa] = int(mass)

def Cyclospectrum(Peptide):
    mass = 0
    for aa in Peptide:
        mass += mass_table[aa]
    spectrum = [0, mass]
    temp = Peptide+Peptide
    for i in range(1, len(Peptide)):
        for j in range(len(Peptide)):
            elem = temp[j:j + i]
            mass = 0
            for aa in elem:
                mass += mass_table[aa]
            spectrum.append(mass)
    spectrum.sort()
    return spectrum

def Score(Peptide, Spectrum):
    spec = Cyclospectrum(Peptide)
    score = 0
    all_masses = list(set(spec + Spectrum))
    for mass in all_masses:
        score += min(spec.count(mass), Spectrum.count(mass))
    return score

if __name__ == "__main__":
    import sys
    Peptide,Spectrum = sys.stdin.read().splitlines()
    Spectrum = Spectrum.split(' ')
    for i in range(len(Spectrum)):
        Spectrum[i] = int(Spectrum[i])
    print(Score(Peptide, Spectrum))