mass_file=open('integer_mass_table.txt')
mass_table = {}
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    mass_table[aa] = int(mass)

def LinearSpectrum(Peptide):
    PrefixMass = [0]
    for i in range(len(Peptide)):
        temp = PrefixMass[i] + mass_table[Peptide[i]]
        PrefixMass.append(temp)
    LinearSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
    LinearSpectrum.sort()
    return LinearSpectrum

def LinearScore(Peptide, Spectrum):
    spec = LinearSpectrum(Peptide)
    score = 0
    all_masses = list(set(spec + Spectrum))
    for mass in all_masses:
        score += min(spec.count(mass), Spectrum.count(mass))
    return score

if __name__ == "__main__":
    import sys
    Peptide, Spectrum = sys.stdin.read().splitlines()
    Spectrum = Spectrum.split(' ')
    for i in range(len(Spectrum)):
        Spectrum[i] = int(Spectrum[i])
    print(LinearScore(Peptide, Spectrum))