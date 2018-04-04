import nsfg
import thinkstats2
import thinkplot
import probability

p = nsfg.ReadFemResp()
act_pmf = thinkstats2.Pmf(p.numkdhh, label='actual')
print(act_pmf)

bias_pmf = probability.BiasPmf(act_pmf, label='observed')
print(bias_pmf)

print('Mean number of children, actual: ', act_pmf.Mean())
print('Mean number of children, biased: ', bias_pmf.Mean())

fig = thinkplot.Pmfs([act_pmf, bias_pmf])
#thinkplot.show(xlabel='No. of Children', ylabel='pmf')
thinkplot.SaveFormat(root = 'act_vs_biased',
               fmt = 'png',
               xlabel = 'No. of Children',
               ylabel = 'pmf')
