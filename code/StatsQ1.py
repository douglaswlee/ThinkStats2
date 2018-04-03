import first
import math
import numpy as np

def cohens_d(g1, g2):
    #n1 = g1.size - g1.isnull().sum()
    #n2 = g2.size - g2.isnull().sum()
    n1 = len(g1.dropna())
    n2 = len(g2.dropna())
    if n1 == 0 or n2 == 0:
        return np.nan
    else:
        v_pooled = math.sqrt(((n1-1)*g1.var() + (n2-1)*g2.var())/(n1+n2-2))
        d = (g1.mean() - g2.mean())/v_pooled
        return d

#def main():
live, firsts, others = first.MakeFrames()

print(firsts.totalwgt_lb.mean())
print(others.totalwgt_lb.mean())

d_totalwgt_lb = cohens_d(firsts.totalwgt_lb, others.totalwgt_lb)
d_prglngth = cohens_d(firsts.prglngth, others.prglngth)

print('Cohen\'s d for total weight: ', d_totalwgt_lb)
print('Cohen\'s d fro pregnancy length: ', d_prglngth)

#if __name__ == '__main__':
#    main()
