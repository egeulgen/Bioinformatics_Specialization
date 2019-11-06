def reverse_comp(Seq):
    return Seq[::-1].translate(Seq.maketrans('ATCG', 'TAGC'))

def SharedKmers(k, seq1, seq2):
    result = []
    seq1dict = {}
    for i in range(len(seq1) - k + 1):
        key = seq1[i:i+k]
        if key in seq1dict.keys():
            seq1dict[key].append(i)
        elif reverse_comp(key) in seq1dict.keys():
            seq1dict[reverse_comp(key)].append(i)
        else:
            seq1dict[key] = [i]
    for j in range(len(seq2) - k + 1):
        sub2 = seq2[j:j+k]
        if sub2 in seq1dict.keys():
            for pos in seq1dict[sub2]:
                result.append([pos, j])
        elif reverse_comp(sub2) in seq1dict.keys():
            for pos in seq1dict[reverse_comp(sub2)]:
                result.append([pos, j])
    return result

if __name__ == "__main__":
    k = int(input().rstrip())
    seq1 = input().rstrip()
    seq2 = input().rstrip()
    result = SharedKmers(k, seq1, seq2)
    for r in result:
        print('(' + ', '.join(map(str, r)) + ')')
    print(' ')
    print(' ')
    print(' ')
    print(len(result))
    # file = open('E_coli.txt', 'r')
    # seq1 = file.read().rstrip()
    # file = open('Salmonella_enterica.txt', 'r')
    # seq2 = file.read().rstrip()
    # result = SharedKmers(30, seq1, seq2)

    # with open('pHCM1.txt') as f:
    #     lines = f.readlines()
    #     pHCM1 = [line.strip() for line in lines]
    # seq3 = ''
    # for line in pHCM1:
    #     seq3 += line

    # with open('pHCM2.txt') as f:
    #     lines = f.readlines()
    #     pHCM2 = [line.strip() for line in lines]
    # seq4 = ''
    # for line in pHCM2:
    #     seq4 += line

    # result2 = SharedKmers(30, seq1, seq3)
    # result3 = SharedKmers(30, seq1, seq4)

    # print(len(result) + len(result2) + len(result3))