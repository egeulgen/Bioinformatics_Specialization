masses=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def CountPeptides(Mass):
    NumPeptides={}
    for i in range(57):
        NumPeptides[i] = 0
    for mass in range(57, Mass + 1):
        NumPeptides[mass] = masses.count(mass)
        for i in range(len(masses)):
            if mass >= masses[i]:
                if NumPeptides[mass - masses[i]] > 0:
                    NumPeptides[mass] += NumPeptides[mass - masses[i]]
    return NumPeptides[Mass]