# Wilcoxon signed-rank test
from numpy.random import seed
from scipy.stats import wilcoxon
import random

# seed the random number generator
def evaluate_samples(sample1, sample2):
    seed(1)
    # generate two independent samples
    # compare samples
    stat, p = wilcoxon(sample1, sample2)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Same distribution (fail to reject H0)')
    else:
        print('Different distribution (reject H0)')
