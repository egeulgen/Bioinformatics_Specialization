def NX(LENS, X = .50):
    tot = sum(LENS)
    for L in LENS:
        a = sum([x for x in LENS if x >= L])
        if a >= tot * X:
            NX = L
    return NX

if __name__ == "__main__":
    FASTA_file = open('MRSA_k85/contigs.fasta')
    LENS = []
    for line in FASTA_file:
        if line.startswith('>'):
            LENS.append(int(line.split('length_')[1].split('_')[0]))
    LENS.sort()
    print('N50: ' + str(NX(LENS)))
    count_long = 0
    tot_len_long = 0
    for L in LENS:
        if L >= 1000:
            count_long += 1
            tot_len_long += L
    print('# long contigs: ' + str(count_long))
    print('tot len of long contigs: ' + str(tot_len_long))