err_rate = 0.3

mass_file=open('integer_mass_table.txt')
mass_table = {}
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    mass_table[aa] = int(mass)

def get_blocks(values, err_rate = err_rate):
    mi, ma = 0, 0
    result = []
    temp = []
    for v in sorted(values):
        if not temp:
            mi = ma = v
            temp.append(v)
        else:
            if abs(v - mi) < err_rate and abs(v - ma) < err_rate:
                temp.append(v)
                if v < mi:
                    mi = v
                elif v > ma:
                    ma = v
            else:
                if len(temp) > 1:
                    result.append(temp)
                mi = ma = v
                temp = [v]
    return result

def Convolution(Spectrum, lower_lim = 57, upper_lim = 200):
    conv = []
    for i in range(len(Spectrum) - 1):
        for j in range(i, len(Spectrum)):
            diff = Spectrum[j] - Spectrum[i]
            if diff >= lower_lim and diff <= upper_lim:
                conv.append(diff)
    conv.sort()
    return conv

def Alphabet(Spectrum, M):
    convolution = Convolution(Spectrum)
    blocks = get_blocks(convolution)
    freq_dict = {}
    for block in blocks:
        aa = round(block[0])
        freq_dict[aa] = len(block)
    sorted_elems = sorted(freq_dict.items(), key=lambda kv: kv[1], reverse = True)
    alphabet = sorted_elems[:M]
    if sorted_elems[M][1] == alphabet[-1][1]:
        idx = M
        while sorted_elems[idx][1] == alphabet[-1][1] and idx < len(sorted_elems):
            alphabet.append(sorted_elems[idx])
            idx += 1
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i][0]
    alphabet.sort()
    return alphabet

class Peptide:
    def __init__(self):
        self.sequence = []
        self.mass = 0
        self.score = 0
    def LinearSpectrum(self):
        PrefixMass = [0]
        for i in range(len(self.sequence)):
            temp = PrefixMass[i] + self.sequence[i]
            PrefixMass.append(temp)
        LinearSpectrum = [0]
        for i in range(len(self.sequence)):
            for j in range(i + 1, len(self.sequence) + 1):
                LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
        LinearSpectrum.sort()
        return LinearSpectrum
    def Cyclospectrum(self):
        mass = sum(self.sequence)
        spectrum = [0, mass]
        temp = self.sequence + self.sequence
        for i in range(1, len(self.sequence)):
            for j in range(len(self.sequence)):
                elem = temp[j:j + i]
                mass = sum(elem)
                spectrum.append(mass)
        spectrum.sort()
        return spectrum
    def CycloScore(self, Spectrum):
        spec = self.Cyclospectrum()
        score = 0
        for mass in Spectrum:
            Aprrox_Count_pep = 0
            for m in spec:
                if m >= mass - err_rate and m <= mass + err_rate:
                    Aprrox_Count_pep += 1
            Aprrox_Count_spectrum = 0
            for m in Spectrum:
                if m >= mass - err_rate and m <= mass + err_rate:
                    Aprrox_Count_spectrum += 1
            score += min(Aprrox_Count_spectrum, Aprrox_Count_pep)
        return score
    def Score(self, Spectrum):
        if self.sequence == []:
            return 0
        spec = self.LinearSpectrum()
        score = 0
        for mass in Spectrum:
            Aprrox_Count_pep = 0
            for m in spec:
                if m >= mass - err_rate and m <= mass + err_rate:
                    Aprrox_Count_pep += 1
            Aprrox_Count_spectrum = 0
            for m in Spectrum:
                if m >= mass - err_rate and m <= mass + err_rate:
                    Aprrox_Count_spectrum += 1
            score += min(Aprrox_Count_spectrum, Aprrox_Count_pep)
        return score

def Expand(Leaderboard, Spectrum):
    result = []
    for Pep in Leaderboard:
        for mass in MASSES:
            expanded = Peptide()
            expanded.sequence = Pep.sequence + [mass]
            expanded.mass = Pep.mass + mass
            expanded.score = expanded.Score(Spectrum)
            result.append(expanded)
    return result

def Trim(Leaderboard, Spectrum, N):
    if len(Leaderboard) <= N:
        return Leaderboard
    result = []
    scores = []
    for Pep in Leaderboard:
        scores.append(Pep.score)
    sorted_scores = sorted(scores, reverse = True)
    cut_off = sorted_scores[N - 1]
    idx = [i for i,val in enumerate(scores) if val >= cut_off]
    Leaderboard = [Leaderboard[i] for i in idx]
    return Leaderboard

def ConvolutionCyclopeptideSequencing(Spectrum, N):
    LeaderScore = 0
    LeaderPeptide = Peptide()
    LeaderPeptides = []
    Leaderboard = [LeaderPeptide]
    ParentMass = sorted(Spectrum, reverse = True)[round(len(Spectrum) * 10/100)]
    while len(Leaderboard) != 0:
        Leaderboard = Expand(Leaderboard, Spectrum)
        Peptides_to_rem = []
        for Pep in Leaderboard:
            ERR = err_rate
            if Pep.mass >=  ParentMass - ERR and Pep.mass <= ParentMass + ERR:
                PepScore = Pep.CycloScore(Spectrum)
                if PepScore > LeaderScore:
                    LeaderPeptide = Pep
                    LeaderPeptides = [LeaderPeptide.sequence]
                    LeaderScore = PepScore
                    print('NEW BEST: ' + str(PepScore))
                elif PepScore == LeaderScore:
                    LeaderPeptides.append(Pep.sequence) 
            elif Pep.mass > ParentMass + ERR:
                Peptides_to_rem.append(Pep)
        Leaderboard = [x for x in Leaderboard if not x in Peptides_to_rem]
        Leaderboard = Trim(Leaderboard, Spectrum, N)
        print(len(Leaderboard))
        if len(Leaderboard[-1].sequence) == 10:
            break
    return LeaderPeptides

if __name__ == "__main__":
    M = 20
    N = 1000
    file = open('real_spectrum2.txt')
    Spectrum = file.read().rstrip().split(' ')
    for i in range(len(Spectrum)):
        Spectrum[i] = float((Spectrum[i])) - 1.007
    Spectrum.sort()
    Spectrum = [0] + Spectrum
    MASSES = ['F', 'P', 'N', 'Q', 'Y', 'V', 'O', 'L', 'W']
    for i in range(len(MASSES)):
        MASSES[i] = mass_table[MASSES[i]]
    print(MASSES)
    result = ConvolutionCyclopeptideSequencing(Spectrum, N)
    for res in result:
        print(' '.join(map(str, res)))
    