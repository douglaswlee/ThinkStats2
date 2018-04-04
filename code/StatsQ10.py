import thinkstats2
import thinkplot
import estimation
import math
import numpy as np

def SimulateGame(lam):
    t = 0
    goals = 0

    while True:
        x = np.random.exponential(1.0/lam, 1)
        t += x
        if t < 1:
            goals += 1
        else:
            break
    return goals

def EstimateGoals(lam, m):
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    lams = []
    for _ in range(m):
        goals = SimulateGame(lam)
        lams.append(goals)

    print('RMSE of Goals: ', estimation.RMSE(lams, lam))
    print('Mean Error of Goals: ', estimation.MeanError(lams, lam))

    cdf = thinkstats2.Cdf(lams)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    VertLine(ci[0])
    VertLine(ci[1])
    
    thinkplot.Cdf(cdf)
    #thinkplot.Show(xlabel = 'Goals', ylabel = 'CumProb', title = 'Sampling Distribution, lam = ' + str(lam))
    thinkplot.SaveFormat(root = 'Q9_sampling_dist',
                         fmt = 'png',
                         xlabel = 'Goals',
                         ylabel = 'CumProb',
                         title = 'Sampling Distribution, lam = ' + str(lam))

thinkstats2.RandomSeed(1)
EstimateGoals(5, 1000)
    
