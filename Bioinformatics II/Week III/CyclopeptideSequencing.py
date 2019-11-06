MASSES = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def Expand(Peptides):
    expanded = []
    for peptide in Peptides:
        for mass in MASSES:
            expanded.append(peptide + [mass])
    return expanded

def Cyclospectrum(Peptide):
    mass = sum(Peptide)
    spectrum = [0, mass]
    temp = Peptide + Peptide
    for i in range(1, len(Peptide)):
        for j in range(len(Peptide)):
            elem = temp[j:j + i]
            mass = sum(elem)
            spectrum.append(mass)
    spectrum.sort()
    return spectrum

def LinearSpectrum(Peptide):
    PrefixMass = [0]
    for i in range(len(Peptide)):
        temp = PrefixMass[i] + Peptide[i]
        PrefixMass.append(temp)
    LinearSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
    LinearSpectrum.sort()
    return LinearSpectrum

def Consistent(Peptide, Spectrum):
    if sum(Peptide) > Spectrum[-1] - MASSES[0]:
        return False
    spec = LinearSpectrum(Peptide)
    for mass in spec:
        if not mass in Spectrum:
            return False
    return True

def CyclopeptideSequencing(Spectrum):
    Peptides = [[]]
    result = []
    while len(Peptides) != 0:
        Peptides = Expand(Peptides)
        for Peptide in Peptides:
            if sum(Peptide) == Spectrum[-1]:
                if Cyclospectrum(Peptide) == Spectrum:
                    result.append(Peptide)
                Peptides = [x for x in Peptides if x != Peptide]
            elif not Consistent(Peptide, Spectrum):
                Peptides = [x for x in Peptides if x != Peptide]
    return result

if __name__ == "__main__":
    import sys
    Spectrum = sys.stdin.read().rstrip().split(' ')
    for i in range(len(Spectrum)):
        Spectrum[i] = int(Spectrum[i])
    res = CyclopeptideSequencing(Spectrum)
    for i in range(len(res)):
        res[i] = '-'.join(map(str, res[i]))
    print(' '.join(res))