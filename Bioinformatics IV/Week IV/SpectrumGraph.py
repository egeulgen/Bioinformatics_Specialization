import sys

mass_file=open('integer_mass_table.txt')
mass_table = {}
for line in mass_file:
    aa, mass = line.rstrip().split(' ')
    mass_table[int(mass)] = aa


def SpectrumGraph(spectrum):
    adj_list = []
    for i in range(len(spectrum)):
        for j in range(i, len(spectrum)):
            if spectrum[j] - spectrum[i] in mass_table.keys():
                adj_list.append([spectrum[i], spectrum[j], mass_table[spectrum[j] - spectrum[i]]])
    return adj_list

if __name__ == "__main__":
    spectrum = sys.stdin.read().rstrip()
    spectrum = [int(s) for s in spectrum.split(' ')]
    spectrum = [0] + spectrum
    
    adj_list = SpectrumGraph(spectrum)
    for edge in adj_list:
        print(str(edge[0]) + '->' + str(edge[1]) + ':' +  str(edge[2]))