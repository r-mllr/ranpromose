from Bio import SeqIO
from random import SystemRandom

sys_random = SystemRandom()


def get_sequences(fasta_file):
    """
    fasta_file: file in fasta format
    returns sequences as list
    """
    return list(SeqIO.parse(fasta_file, "fasta"))


def generate_sequence(t, n, l1, d1, l2, d2, spacer):
    """
    generate t sequences with length n
    l1: first motif length
    d1: number of mutations in Motif 1
    l2: right motig length
    d2: number of mutations in Motif 2
    spacer: length of spacer
    """
    m1 = random_sequence(l1)
    m2 = random_sequence(l2)
    return [fill_sequence(mutate(m1, d1) +
            mutate(random_sequence(spacer)) +
            mutate(m2, d2), n) for _ in range(t)]


def random_sequence(k=int()):
    """
    generates a random sequence with length k
    """
    return ''.join(sys_random.choice('ACGT') for _ in range(k))


def mutate(seq, d=1):
    """
    mutate given sequence with d mutations
    """
    s = list(seq)
    for _ in range(d):
        i = sys_random.randrange(len(seq))
        s[i] = mutate_nuc(s[i])
    return "".join(s)


def mutate_nuc(nuc):
    c = sys_random.choice("ACGT_*")
    if(c == "_"):
        return ""
    elif(c == "*"):
        return "{}{}".format(nuc, sys_random.choice('ACGT'))
    else:
        return c


def fill_sequence(seq, n):
    while(len(seq) < n):
        i = sys_random.randint(0, 1)
        c = sys_random.choice("ACGT")
        if i == 0:
            seq = c + seq
        else:
            seq = seq + c
    return seq


def edit_distance(seq1, seq2):
    seq1 = [" "] + list(seq1)
    seq2 = [" "] + list(seq2)
    m = [[0 for _ in seq2] for _ in seq1]
    for i, s1 in enumerate(seq1):
        for j, s2 in enumerate(seq2):
            if i == 0:
                m[i][j] = j
            elif j == 0:
                m[i][j] = i
            elif s1 == s2:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = 1 + min(
                        m[i-1][j],
                        m[i][j-1],
                        m[i-1][j-1]
                        )
    return m[len(seq1)-1][len(seq2)-1]
