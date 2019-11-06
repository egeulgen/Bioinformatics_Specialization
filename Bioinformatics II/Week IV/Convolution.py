def Convolution(Spectrum):
    Spectrum.sort()
    conv = []
    for i in range(len(Spectrum) - 1):
        for j in range(i, len(Spectrum)):
            diff = Spectrum[j] - Spectrum[i]
            if diff != 0:
                conv.append(diff)
    return conv

if __name__ == "__main__":
    import sys
    Spectrum = sys.stdin.read().rstrip()
    Spectrum = Spectrum.split(' ')
    for i in range(len(Spectrum)):
        Spectrum[i] = int(Spectrum[i])
    print(' '.join(map(str, Convolution(Spectrum))))