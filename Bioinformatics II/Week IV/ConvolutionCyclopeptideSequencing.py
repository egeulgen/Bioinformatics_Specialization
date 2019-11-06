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
    freq_dict = {}
    for aa in convolution:
        if aa in freq_dict.keys():
            freq_dict[aa] += 1
        else:
            freq_dict[aa] = 1
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
        all_masses = list(set(spec + Spectrum))
        for mass in all_masses:
            score += min(spec.count(mass), Spectrum.count(mass))
        return score
    def Score(self, Spectrum):
        if self.sequence == []:
            return 0
        spec = self.LinearSpectrum()
        score = 0
        all_masses = list(set(spec + Spectrum))
        for mass in all_masses:
            score += min(spec.count(mass), Spectrum.count(mass))
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
    ParentMass = Spectrum[-1]
    while len(Leaderboard) != 0:
        Leaderboard = Expand(Leaderboard, Spectrum)
        Peptides_to_rem = []
        for Pep in Leaderboard:
            if Pep.mass == ParentMass:
                PepScore = Pep.CycloScore(Spectrum)
                if PepScore > LeaderScore:
                    LeaderPeptide = Pep
                    LeaderPeptides = [LeaderPeptide.sequence]
                    LeaderScore = PepScore
                    print('NEW BEST: ' + str(PepScore))
                elif PepScore == LeaderScore:
                    LeaderPeptides.append(Pep.sequence) 
            elif Pep.mass > ParentMass:
                Peptides_to_rem.append(Pep)
        Leaderboard = [x for x in Leaderboard if not x in Peptides_to_rem]
        Leaderboard = Trim(Leaderboard, Spectrum, N)
        print(len(Leaderboard))
    return LeaderPeptides

if __name__ == "__main__":
    import sys
    M, N, Spectrum = sys.stdin.read().splitlines()
    M = int(M)
    N = int(N)
    Spectrum = Spectrum.split(' ')
    for i in range(len(Spectrum)):
        Spectrum[i] = int(Spectrum[i])
    Spectrum.sort()
    MASSES = Alphabet(Spectrum, M)
    result = ConvolutionCyclopeptideSequencing(Spectrum, N)
    answer = []
    for res in result:
        answer.append('-'.join(map(str, res)))
    print(' '.join(answer))