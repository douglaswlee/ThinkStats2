import math
import thinkstats2
import thinkplot
import estimation
import numpy as np

def Simulate_Sample(lam, n, m=1000):
    means = []
    medians = []

    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1/np.mean(xs)
        means.append(L)

    cdf = thinkstats2.MakeCdfFromList(means)
    stderr = estimation.RMSE(means, lam)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    return cdf, stderr, ci

thinkstats2.RandomSeed(1)
ns = np.arange(10, 1000, 10)
stderrs = []
cis = []
cdfs = []
for n in ns:
    cdf, stderr, ci = Simulate_Sample(2, n, m=1000)
    cdfs.append(cdf)
    stderrs.append(stderr)
    cis.append(ci)

print('Standard error, n = 10: ', stderrs[0])
print('Confidence interval, n = 10: ', cis[0])

idx = [i for i,x in enumerate(ns) if x == 100]
print('Standard error, n = 100: ', stderrs[list(ns).index(100)])
print('Confidence interval, n = 100: ', cis[list(ns).index(100)])

print('Standard error, n = 1000: ', stderrs[-1])
print('Confidence interval, n = 1000: ', cis[-1])

thinkplot.Cdf(cdfs[0])
thinkplot.Show(xlabel='x', ylabel='CumProb')

thinkplot.Plot(ns, stderrs)
thinkplot.Show(xlabel='n', ylabel='Standard Error')
