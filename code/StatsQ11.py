import first
import hypothesis
import thinkplot
import thinkstats2
import numpy as np

class DiffMeansResample(hypothesis.DiffMeansPermute):

    def RunModel(self):
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2    

live, firsts, others = first.MakeFrames()
data1 = firsts.prglngth.values, others.prglngth.values

#thinkstats2.RandomSeed(1)
ht1 = DiffMeansResample(data1)
p_prglngth = ht1.PValue()

#thinkstats2.RandomSeed(1)
data2 = firsts.totalwgt_lb.dropna().values, others.totalwgt_lb.dropna().values
ht2 = DiffMeansResample(data2)
p_totalwgt_lb = ht2.PValue()
