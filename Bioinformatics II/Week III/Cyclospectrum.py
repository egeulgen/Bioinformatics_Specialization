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

if __name__ == "__main__":
    import sys
    Peptide = sys.stdin.read().rstrip()
    res = Cyclospectrum(Peptide)
    print(' '.join(map(str, res)))

# SPEC = '0 71 101 113 131 184 202 214 232 285 303 315 345 416'
# SPEC = SPEC.split(' ')
# for i in range(len(SPEC)):
#     SPEC[i] = int(SPEC[i])

SPEC = '0 71 99 101 103 128 129 199 200 204 227 230 231 298 303 328 330 332 333'
SPEC = SPEC.split(' ')
for i in range(len(SPEC)):
    SPEC[i] = int(SPEC[i])

def Consistent(Peptide, SPEC = SPEC):
    masses = LinearSpectrum(Peptide)
    for mass in masses:
        if not mass in SPEC:
            return False
    return True