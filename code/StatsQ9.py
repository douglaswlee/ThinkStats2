import hinc
import hinc2
import thinkstats2
import thinkplot
import numpy as np

df = hinc.ReadData()

def describe_inc_dist(log_upper):
    log_sample = hinc2.InterpolateSample(df, log_upper=j)
    incomes = np.power(10, log_sample)

    inc_mean = thinkstats2.Mean(incomes)
    inc_med = thinkstats2.Median(incomes)
    inc_skew = thinkstats2.Skewness(incomes)
    inc_pearskew = thinkstats2.PearsonMedianSkewness(incomes)
    print('log_upper = ', j)
    print('Mean Income: ', inc_mean)
    print('Median Income: ', inc_med)
    print('Skewness: ', inc_skew)
    print('Pearson Median Skewness: ', inc_pearskew)

    cdf = thinkstats2.Cdf(incomes)
    inc_below_mean = cdf.Prob(inc_mean)
    print('Pct. below mean: ', inc_below_mean)
    print('\n')

for j in [6.0, 7.0, 8.0]:
    describe_inc_dist(log_upper = j)

    
