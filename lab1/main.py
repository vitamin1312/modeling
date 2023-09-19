from stats import *
from utils import nums_to_file, nums_from_file
from time import time

SEED = int(time())
# SEED = 2023
if __name__ == '__main__':

    nums = lemers_method(SEED)
    nums_to_file(nums, 'data.txt')
    plot_hist_F(nums, 'hist', 'F')
    print('stats for alpha = 1%')
    print('===========================================================')
    print('series method |z| < 2.8')
    print('series method', series(nums))
    print('===========================================================')
    print('chi-squared^-1(0.99, 197) = 243.8595')
    print('chi-squared value:', chi_square(nums))
    print('===========================================================')
    print('K^-1(0.005) = 0.41709; k^-1(0.995) = 1.73083')
    print('kolmogorov value:', kolmogorov(nums))
