import nsfg
import thinkstats2
import thinkplot

import random
import pandas as pd
import numpy as np

def rand_list(n):
    rands = [random.random() for _ in range(n)]
    return rands

rands = rand_list(1000)
pmf = thinkstats2.Pmf(rands)
cdf = thinkstats2.Cdf(rands)

thinkplot.Pmf(pmf)
thinkplot.Show(xlabel='x', ylabel='pmf')
#thinkplot.Save(root = 'Q4_2pmf',
#               xlabel = 'x',
#               ylabel = 'Prob')

thinkplot.Cdf(cdf)
thinkplot.Show(xlabel = 'x', ylabel = 'cdf')
#thinkplot.Save(root = 'Q4_2cdf',
#            xlabel = 'x',
#            ylabel = 'CumProb')
