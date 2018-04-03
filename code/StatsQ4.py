import scipy.stats

def in_to_cm(inches):
    return inches * 2.54

def norm_cdf_slice(a, b, mu, sigma):
    F_a = scipy.stats.norm.cdf(a, loc=mu, scale=sigma)
    F_b = scipy.stats.norm.cdf(b, loc=mu, scale=sigma)
    return F_b - F_a

mean_ht_cm = 178
sd_ht_cm = 7.7
a = in_to_cm(70)
b = in_to_cm(73)
pct_blue = norm_cdf_slice(a, b, mean_ht_cm, sd_ht_cm)
print('The percentage of blue men is: ', pct_blue)
