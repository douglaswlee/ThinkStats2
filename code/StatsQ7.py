import thinkstats2
import thinkplot
import first
import numpy as np

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

rho = thinkstats2.Corr(live.agepreg, live.totalwgt_lb)
rho_s = thinkstats2.SpearmanCorr(live.agepreg, live.totalwgt_lb)
print('Pearson\'s Correlation, Mother\'s age and Birth weight: ', rho)
print('Spearman\'s Rank Correlation, Mother\'s age and Birth weight: ', rho_s)

thinkplot.LEGEND = False
thinkplot.Scatter(live.agepreg, live.totalwgt_lb)
thinkplot.Show(xlabel = 'Mother\'s age', ylabel = 'Birth weight')

thinkplot.LEGEND = True
bins = np.arange(10, 45, 2.5)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)
ages = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weights, label = label)
thinkplot.Show(xlabel = 'Mother\'s age', ylabel = 'Birth weight')
