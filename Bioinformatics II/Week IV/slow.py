MASSES = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

class Peptide:
    def __init__(self):
        self.sequence = []
        self.mass = 0
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
    def Score(self, Spectrum):
        if self.sequence == []:
            return 0
        spec = self.LinearSpectrum()
        score = 0
        all_masses = list(set(spec + Spectrum))
        for mass in all_masses:
            score += min(spec.count(mass), Spectrum.count(mass))
        return score

def Expand(Leaderboard):
    result = []
    for Pep in Leaderboard:
        for mass in MASSES:
            expanded = Peptide()
            expanded.sequence = Pep.sequence + [mass]
            expanded.mass = Pep.mass + mass
            result.append(expanded)
    return result

def Trim(Leaderboard, Spectrum, N):
    if len(Leaderboard) <= N:
        return Leaderboard
    result = []
    scores = []
    for Pep in Leaderboard:
        scores.append(Pep.Score(Spectrum))
    sorted_scores = sorted(scores, reverse = True)
    cut_off = sorted_scores[N - 1]
    idx = [i for i,val in enumerate(scores) if val >= cut_off]
    Leaderboard = [Leaderboard[i] for i in idx]
    return Leaderboard

def LeaderboardCyclopeptideSequencing(Spectrum, N):
    LeaderPeptide = Peptide()
    Leaderboard = [LeaderPeptide]
    ParentMass = Spectrum[-1]
    while len(Leaderboard) != 0:
        Leaderboard = Expand(Leaderboard)
        Peptides_to_rem = []
        LeaderScore = LeaderPeptide.Score(Spectrum)
        for Pep in Leaderboard:
            if Pep.mass == ParentMass:
                if Pep.Score(Spectrum) > LeaderScore:
                    LeaderPeptide = Pep
            elif Pep.mass > ParentMass:
                Peptides_to_rem.append(Pep)
        Leaderboard = [x for x in Leaderboard if not x in Peptides_to_rem]
        Leaderboard = Trim(Leaderboard, Spectrum, N)
        print(len(Leaderboard))
    return LeaderPeptide.sequence

if __name__ == "__main__":
    import sys
    N, Spectrum = sys.stdin.read().splitlines()
    N = int(N)
    N = 10
    Spectrum = Spectrum.split(' ')
    for i in range(len(Spectrum)):
        Spectrum[i] = int(Spectrum[i])
    res = LeaderboardCyclopeptideSequencing(Spectrum, N)
    print('-'.join(map(str, res)))