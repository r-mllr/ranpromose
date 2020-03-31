# app.py
from collections import Counter
from random import SystemRandom
import ranpromose.resources.sequence as seqm

sys_random = SystemRandom()


class Ranpromose:

    @staticmethod
    def run():
        seqs, m1, m2 = seqm.generate_sequence(20, 50, 8, 2, 6, 2, 15)
        lmer_size = 8
        maxis = Counter()
        for _ in range(1000):
            counter = Counter()
            for s in seqs:
                lmers = seqm.kmers(s, lmer_size)
                random_pick = sys_random.sample(range(0, lmer_size), 5)
                lmers = [seqm.project(seq, indexes=random_pick) for seq in lmers]
                counter += Counter(lmers)
            maxis += counter
        print(maxis)
        print(m1, m2)
        print("Hello World!")
