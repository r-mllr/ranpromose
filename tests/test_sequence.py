import numpy as np
import ranpromose.resources.sequence as seqm


def test_generate_sequences():
    seqs = seqm.generate_sequence(5, 50, 8, 2, 6, 2, 15)
    assert len(seqs) == 5
    for s in seqs:
        assert len(s) == 50


def test_random_sequence():
    for i in (1, 5, 100):
        seq = seqm.random_sequence(i)
        assert len(seq) == i


def test_mutate():
    for i in (5, 10, 100):
        seq = seqm.random_sequence(i)
        distances = [seqm.edit_distance(seq, seqm.mutate(seq, 4)) for _ in range(100)]
        assert np.max(distances) == 4


def test_edit_distance():
    seq1 = ("AAAAA", "AAAA", "ATGC", "A", "")
    seq2 = ("AAAA", "AAAT", "G", "T", "ATGC")
    exp = (1, 1, 3, 1, 4)
    for s1, s2, e in zip(seq1, seq2, exp):
        assert seqm.edit_distance(s1, s2) == e


def test_fill_sequence():
    s = ("", "ATGCC", "AAAAAAAAAAAAA")
    for i in s:
        assert len(seqm.fill_sequence(i, 50)) == 50
