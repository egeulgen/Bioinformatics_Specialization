# MASSES = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
MASSES = list(range(57,201))

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

def LeaderboardCyclopeptideSequencing(Spectrum, N):
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
    N, Spectrum = sys.stdin.read().splitlines()
    N = int(N)
    Spectrum = Spectrum.split(' ')
    for i in range(len(Spectrum)):
        Spectrum[i] = int(Spectrum[i])
    result = LeaderboardCyclopeptideSequencing(Spectrum, N)
    answer = []
    for res in result:
        answer.append('-'.join(map(str, res)))
    print(' '.join(answer))